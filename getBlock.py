import requests
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")

# dblist = myclient.list_database_names()
# print(dblist)

mydb = myclient["DB"]
block = mydb["Blocks"]w
user = mydb["User"]

headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}

blockCnt = 12000001
# blockCnt = 12000153
# 14845505	
for index in range(12000050, 120000051):
    print(index)
    url = "https://deep-index.moralis.io/api/v2/block/" + str(index) + "?chain=eth"
    r = requests.get(url = url, headers = headers)
    # dict = json.loads(r.text())
    print(len(r.json()['transactions']))
    print(r.json()['transactions'][0]['from_address'])
    print(r.json()['transactions'][0]['to_address'])

    # x = block.insert_one(r.json())

    # print(x.inserted_id)

    

# print(url)
# url = "https://deep-index.moralis.io/api/v2/block/12000000/nft/transfers?chain=eth"


