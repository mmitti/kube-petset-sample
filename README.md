# kube-petset-sample
KubernetesのPetSetの挙動を確認するために作成したサンプルです。  
2つのコンテナで構成されています。
## test-db
DBコンテナとして作成しました。（実際はただのjsonファイルを読み書きするAPIサーバーです。  
5000番ポートにHTTPアクセスするとjsonの内容を取得したり追記したり出来ます。  
