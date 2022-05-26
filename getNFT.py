from audioop import add
import requests
# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# mydb = myclient["DB"]
# block = mydb["Blocks"]
address = "0x4c6007e38ce164ed80ff8ff94192225fcdac68cd"
headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}
url = "https://deep-index.moralis.io/api/v2/" + address + "/nft?chain=eth"
r = requests.get(url = url, headers = headers)
print(r.text)

