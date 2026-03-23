"""
here i compare result of both default and
custome headers.
"""

# -------------------------------------------------

import requests

# -------------------------------------------------

# no custome headers --- default request

try:
    response1 = requests.get("https://api.github.com")

    print("Status code:", response1.status_code)

    # python-requests/2.32.5
    print("Default Agent:", response1.request.headers.get("User-Agent"))

    # none
    print("Default Content-type:", response1.request.headers.get("Content-Type"))


except Exception as e:
    print("Error:", e)


# -------------custome headers----------------------

headers = {
    "User-Agent": "Chrome/5.0 (Windows NT 11.0)",
    "Accept": "application/json"
}

try:

    response2 = requests.get("https://api.github.com",
                            headers=headers)

    print("Status code:", response2.status_code)

    # chrome/5.0
    print("Request Agent:", response2.request.headers.get("User-Agent"))

    # none
    print("Request Content-type:", response2.request.headers.get("Content-Type"))

    # application/json
    print("Response Content-type:", response2.headers.get("Content-Type"))


except Exception as e:
    print("Error:", e)    