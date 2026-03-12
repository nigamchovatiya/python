"""
requests library: GET and POST requests, headers, 
status codes, parsing JSON responses
 
200 - Success
201 - Resource Created
204 - Success but no response
 
301 — Moved Permanently
302 — Found (Temporary Redirect)
 
400 — Bad Request
401 — Unauthorized
403 — Forbidden
404 - Not Found
 
500 - Internal server errror
"""
 
# --------------------------------------------------

import requests

# --------------------------------------------------

 
url = 'https://api.restful-api.dev/objects/'
 
try: 
    # send get request
    response = requests.get(url)

    # response convert json
    data = response.json()
    print(data)
    # print(type(data))
 
    # create a new data to send api
    data = {
        "name": "lenovo Laptop",
        "data": {
            "year": 2024,
            "price": 120000,
            "CPU model": "Intel i7",
            "Hard disk size": "1 TB"
        }
    }
 
    header = {
        "Content-Type": "application/json"
    }
 
    # this send data in api server
    response = requests.post(url, json=data, headers=header)

    print(response.status_code)
    print(response.json())
    print(response.headers)


except Exception as e:
    print("Unexpeced Error:", e)    

