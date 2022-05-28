import json
import requests
import csv
import pymogo


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["DB"]
block = mydb["Blocks"]
user = mydb["User"]

data = []

url = "https://deep-index.moralis.io/api/v2/"
headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}

with open("userAddressSimple.json", "r", encoding='utf-8') as jsonf:
    data = json.load(jsonf)
    # print(userAddress)

for items in data:
    
    r = requests.get(url+str(items['Address'])+"/erc20", headers=headers)
    foo = json.loads(r.text)
    items["ERC20s"] = foo
    
    r = requests.get(url+str(items['Address'])+"/erc20/transfers", headers=headers)
    foo = json.loads(r.text)
    items["ERC20sHistory"] = foo

    r = requests.get(url+str(items['Address'])+"/nft", headers=headers)
    foo = json.loads(r.text)
    items["NFTs"] = foo
    
    r = requests.get(url+str(items['Address'])+"/nft/transfers", headers=headers)
    foo = json.loads(r.text)
    items["NFTHistory"] = foo

    x = user.insert_one(data)
    # print(items)

    # print(r.text)


# with open("UsersInfo.json", 'w', encoding='utf-8') as jsonf: 
#     jsonString = json.dumps(data, indent=4)
#     jsonf.write(jsonString)




# with open("foo.CSV") as csvFile:
#     csvReader = csv.DictReader(csvFile)
#     for row in csvReader:
#         # print(row['Address'])
#         r = requests.get(url+str(row['Address'])+"/erc20", headers=headers)
#         print(r.status_code)
#         if (r.status_code == 200):
#             foo = json.loads(r.text)
#             data.append(foo)


