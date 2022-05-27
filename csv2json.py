from email import header
import json
import requests
import csv

data = []

url = "https://deep-index.moralis.io/api/v2/"
headers = {"X-API-Key": "MJR9J19aQ2DKtfoY69Qe2DrhjmufP6IQa46HeHWlNGd6TmaOyMP3RKtjMksMfe5Y"}

with open("foo.CSV") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        print(row['Address'])
        r = requests.get(url+str(row['Address']), headers=headers)
        
        data.append(r.text)

print(data)
# with open("users_simplify.json", 'w', encoding='utf-8') as jsonf: 
#     jsonString = json.dumps(data, indent=4)
#     jsonf.write(jsonString)
# print(data)
# with open()