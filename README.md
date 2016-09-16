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
