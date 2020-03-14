Qiitaに記事を投稿しています．
[森久保乃々のネガティブ度を感情分析してみましたけど...。【ポジパと比較】](https://qiita.com/ysk0832/items/b30ab6697389ee5aa45a)

# 使い方
1. アクセストークン取得（アカウント情報は[こちら](https://api.ce-cotoha.com/home)から確認）
```
curl -X POST -H "Content-Type:application/json" -d '{
  "grantType": "client_credentials",
  "clientId": "自分のクライアントID",
  "clientSecret": "自分のクライアントシークレット"
}' https://api.ce-cotoha.com/v1/oauth/accesstokens
```
2. `scraping_morikubo.py`でセリフをスクレイピングする．このとき`speeches_morikubo.txt`が作成される．
3. `sentiment_analysis.py`でCOTOHA APIによる感情分析を行う．
<font color="Red">各APIは1000コール/日なので注意．</font> 結果は`result_morikubo.txt`のようになる．
