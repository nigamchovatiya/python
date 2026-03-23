"""
here i fetch free api github.com and print
status code and headers.
"""

# ----------------------------------------------------

import requests

# ----------------------------------------------------

try:
    response = requests.get('https://api.github.com')

    # status code 200 ok 
    print("Status Code: ", response.status_code)

    # header info print
    print("Headers: ", response.headers)


except Exception as e:
    print("Error:", e)    