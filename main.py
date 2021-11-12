import requests, json
import matplotlib.pyplot as plt

url = "https://api.hahow.in/api/group/photography/courses?page=1"
pages = []
title = []
price = []
comments = []
people = []
# resjson = {}
count = 0
for i in range(1,4):
    res = requests.get(f"https://api.hahow.in/api/group/photography/courses?page={i}", headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})
    resjson = json.loads(res.text)
    for i in resjson['data']:
        title.append(i["title"])
        price.append(i["price"])
        people.append(i["numRating"])
        comments.append(i["numSoldTickets"])
pages.append(resjson)

'''
for i in range(1,len(title)):
    for j in title,price,people,comments:
        print(j[i])
'''

for i in range(len(price)):
    for j in range((i + 1),len(price)):
        if(price[i] > price[j]): # 如果要按照人數的話就把這裡改成people
            price[i], price[j] = price[j], price[i]
            title[i], title[j] = title[j], title[i]
            comments[i], comments[j] = comments[j], comments[i]
            people[i], people[j] = people[j], people[i]

for i in range(1,len(title)):
    for j in title,price,people,comments:
        print(str(j[i]), end = " \t")
    print()

