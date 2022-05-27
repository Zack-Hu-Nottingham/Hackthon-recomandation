import json
import requests


data = []

with open("foo.CSV") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        # print(row['Address'])
        r = requests.get(url+str(row['Address'])+"erc20", headers=headers)
        foo = json.loads(r.text)
        data.append(foo)


address = "0x4c6007e38ce164ed80ff8ff94192225fcdac68cd"
headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}
url = "https://deep-index.moralis.io/api/v2/" + address + "/nft?chain=eth"
r = requests.get(url = url, headers = headers)
print(r.text)

