import requests
import json
query=input("What type of news are you interested in ?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-06-24&sortBy=publishedAt&apiKey=d701d87acfc94f698cae0dcf99c5caa5"
r=requests.get(url)
news=json.loads(r.text)
# print(r.text)

for article in news ['articles']:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")
