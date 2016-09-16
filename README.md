# kube-petset-sample
KubernetesのPetSetの挙動を確認するために作成したサンプルです。  
2つのコンテナで構成されています。

## 使い方
```
kubectl create -f pv.yaml
kubectl create -f test-db.yaml
kubectl create -f test-db-client.yaml
```

あとは  
http://kubernetes masterのIP:kubernetes APIのポート番号/api/v1/proxy/namespaces/default/services/test-db-client:5000  
にアクセスすれば動きます。

## アクセスした画面について
![](https://raw.githubusercontent.com/mmitti/kube-petset-sample/master/img.png "サンプル")
- View  
  test-db-clientのホスト名を表示しています。
- API  
  test-dbの現在接続しているホスト名、現在接続しているtest-dbホストが読み込んでいるjsonファイルを生成したホスト名などが表示されています。
- Data
  書き込み処理を行ったtest-dbホスト名(DB HOST)、書き込み処理を要求したtest-db-clientのホスト名(WRITE HOST)、書き込まれたテキストなどが表示されています。  
  なお、テキストをポスト時に処理するtest-db-clientのホストはHTMLを生成しているホストと異なる場合があります。
- テキストボックスとADDボタン
  テキストボックスにテキストを入力してADDボタンを押すとtest-dbサーバーにデータを追加します。

## test-db
DBコンテナとして作成しました。（実際はただのjsonファイルを読み書きするAPIサーバーです。  
8000番ポートにHTTPアクセスするとjsonの内容を取得したり追記したり出来ます。  
こちらはPetSetとして配置することを想定しています。

### /info
>{  
>  "init_time": jsonファイル初期化日時,  
>  "current_host": APIサーバーのホスト名,  
>  "init_host": jsonファイルを初期化したホスト名,  
>  "time": "現在時刻  
>}

### /get
>[{  
>  "dbhost": 書き込みをしたAPIホスト名,  
>  "data": 書き込み内容,  
>  "time": 書き込み日時,  
>  "apihost": 書き込みを行ったtest-db-clientのホスト名  
>}]

### /add
データを追加します。以下のjsonをポストしています。
>{
>  "text":書き込むテキスト,
>  "host":書き込みを行ったtest-db-clientのホスト名
>}

## test-db-client
test-dbと通信してデータを取得しHTMLを生成します。  
こちらは通常のPodとして配置することを想定しています。  
5000番ポートにアクセスするとtest-dbのサービスにアクセスしtest-dbのホストを適当に確定します。  
その後はroom/test-dbのIDにリダイレクトし以降は同じtest-dbにアクセスします。
