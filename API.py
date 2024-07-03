import requests
respons = requests.get("https://fakerapi.it/api/v1/books?_quantity=1")
result = respons.json()
print(result["data"][0]["title"])
print(result["data"][0]["author"])
print(result["data"][0]["genre"])
#print
# (result["data"][0]["address"]["country"])import requests
# respons = requests.get("https://fakerapi.it/api/v1/books?_quantity=1")
# result = respons.json()
# print(result["data"][0]["title"])
# print(result["data"][0]["author"])
# print(result["data"][0]["genre"])
# #print
# # (result["data"][0]["address"]["country"])