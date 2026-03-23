"""
here i use for understanding of working a request
and response object how it's works.
"""

# -----------------------------------------------

import requests
import json

# -----------------------------------------------

""" get request """
response = requests.get("https://api.github.com")

print(response)


# response object
print("Status code", response.status_code) # 200 ok

# print(response.text) # response body 

print("response: ", response.headers) # header info



""" post request """

# url = "https://httpbin.org/post"

# data = {
#     "name": "john",
#     "marks": 95
# }

# # data send using post
# response = requests.post(url, json = data)

# print(response.status_code) # 200
# print(response.json()) # data add show


