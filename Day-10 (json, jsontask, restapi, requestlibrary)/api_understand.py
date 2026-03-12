import requests

url = "https://jsonplaceholder.typicode.com/users"

# python send get request to api
response = requests.get(url)

# response convert in json
data = response.json() 

print(data) # data print
print(type(data)) # list
print(data[0]["name"]) # name of first index
print(data[0]["address"]) # add. of first index
print(response.status_code) # api status code 200 





