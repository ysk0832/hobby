import requests
import json

ACCESS_TOKEN = "アクセストークンを入れる"
API_BASE_URL = "https://api.ce-cotoha.com/api/dev/"


# ----------------------ここから感情分析----------------------
with open("./speeches_morikubo.txt") as f:
    all_speeches = [s.strip() for s in f.readlines()]

positive = {"count": 0, "percentage": 0, "avg": 0}
neutral = {"count": 0, "percentage": 0, "avg": 0}
negative = {"count": 0, "percentage": 0, "avg": 0}

headers = {
    "Content-Type": "application/json",
    "charset": "UTF-8",
    "Authorization": "Bearer {}".format(ACCESS_TOKEN)
}
for s in all_speeches:
    data = {
        "sentence": s
    }
    response = requests.post(API_BASE_URL+"nlp/v1/sentiment",
                                headers=headers,
                                data=json.dumps(data))
    result = response.json()

    sentiment = result['result']['sentiment']
    score = result['result']['score']
    print(sentiment+" : "+str(score))
    if sentiment=="Positive":
        positive["count"]+=1
        positive["avg"]+=score
    if sentiment=="Neutral":
        neutral["count"]+=1
        neutral["avg"]+=score
    if sentiment=="Negative":
        negative["count"]+=1
        negative["avg"]+=score
# ----------------------ここまで感情分析----------------------


# ----------------------これ以降は計算と結果表示----------------------
l = len(all_speeches)
print("総セリフ数 : {}".format(l))
positive["percentage"] = positive["count"]/l
neutral["percentage"] = neutral["count"]/l
negative["percentage"] = negative["count"]/l
print("Positive : {}回（{}％）".format(positive["count"],positive["percentage"]*100))
print("Neutral : {}回（{}％）".format(neutral["count"],neutral["percentage"]*100))
print("Negative : {}回（{}％）".format(negative["count"],negative["percentage"]*100))

positive["avg"]/=positive["count"]
neutral["avg"]/=neutral["count"]
negative["avg"]/=negative["count"]
print("平均スコア")
print("Positive : {}".format(positive["avg"]))
print("Neutral : {}".format(neutral["avg"]))
print("Negative : {}".format(negative["avg"]))

print("感情の度合い")
print("Positive : {}".format(positive["percentage"]*positive["avg"]))
print("Neutral : {}".format(neutral["percentage"]*neutral["avg"]))
print("Negative : {}".format(negative["percentage"]*negative["avg"]))
