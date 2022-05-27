import requests
import pymongo
import json

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# mydb = myclient["DB"]
# block = mydb["Blocks"]
# user = mydb["User"]

data = {}
transaction = []
foo = {}

headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}
url = "https://deep-index.moralis.io/api/v2/haoxiao.eth/nft/transfers?chain=eth"

# r = requests.get(url = url, headers = headers)
# print(r.text)

for index in range(12000000, 12000001):
    # print(index)
    url = "https://deep-index.moralis.io/api/v2/block/" + str(index) + "?chain=eth"
    r = requests.get(url = url, headers = headers)
    data["number"] = r.json()['number']
    data["hash"] = r.json()['hash']
    foo[]
    transaction.append()
    print(data)
    # dict = json.loads(r.text())
    # print(len(r.json()['transactions']))
    # print(r.json()['transactions'][0]['from_address'])
    # print(r.json()['transactions'][0]['to_address'])

    # x = block.insert_one(r.json())

    # print(x.inserted_id)

    

# print(url)
# url = "https://deep-index.moralis.io/api/v2/block/12000000/nft/transfers?chain=eth"


