import requests
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["DB"]
blocks = mydb["Blocks"]
blocks_next = mydb["Blocks_14854500_14855000"]
users = mydb["Users"]


url = "https://deep-index.moralis.io/api/v2/"
headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}

addresses = set()

# i = 0
# for block in blocks.find():
#     # i+=1
#     # if i>= 2: break
#     for j in range(len(block['transactions'])):
#         addresses.add(block['transactions'][j]['form_address'])
#         addresses.add(block['transactions'][j]['to_address'])

for block in blocks_next.find():
    for j in range(len(block['transactions'])):
        addresses.add(block['transactions'][j]['form_address'])
        addresses.add(block['transactions'][j]['to_address'])

# data = []

addresses = list(addresses)
print(len(addresses))
# idx = 0
for address in addresses:
    # idx+=1 
    # if (idx >= 10): break
    print(address)

    user = {}
    user["Address"] = str(address)

# for items in data:
    
    r = requests.get(url+str(address)+"/erc20", headers=headers)
    foo = json.loads(r.text)
    user["ERC20s"] = foo
    
    r = requests.get(url+str(address)+"/erc20/transfers", headers=headers)
    foo = json.loads(r.text)
    user["ERC20sHistory"] = foo

    r = requests.get(url+str(address)+"/nft", headers=headers)
    foo = json.loads(r.text)
    user["NFTs"] = foo
    
    r = requests.get(url+str(address)+"/nft/transfers", headers=headers)
    foo = json.loads(r.text)
    user["NFTHistory"] = foo

    x = users.insert_one(user)
# print(len(addresses))