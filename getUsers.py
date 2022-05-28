import requests
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["DB"]
block = mydb["Blocks_14854500_14855000"]
user = mydb["User"]


headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}
url = "https://deep-index.moralis.io/api/v2/haoxiao.eth/nft/transfers?chain=eth"


for index in range(14854500, 14855000):
    print(index)
    data = {}
    transaction = []    # print(index)
    url = "https://deep-index.moralis.io/api/v2/block/" + str(index) + "?chain=eth"
    r = requests.get(url = url, headers = headers)
    data["number"] = r.json()['number']
    data["hash"] = r.json()['hash']

    for idx in range(len(r.json()['transactions'])):
        foo = {}

        foo["hash"] = r.json()['transactions'][idx]['hash']
        foo["form_address"] = r.json()['transactions'][idx]['from_address']
        foo["to_address"] = r.json()['transactions'][idx]['to_address']
        transaction.append(foo)

    data["transactions"] = transaction

    x = block.insert_one(data)

    # with open("blocks.json", 'a', encoding='utf-8') as jsonf: 
    #     jsonString = json.dumps(data, indent=4)
    #     jsonf.write(','+jsonString)


