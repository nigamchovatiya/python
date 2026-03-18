"""
here i fetch a free api currency converter,
and print here.
"""

# ----------------------------------------------

import requests

# ----------------------------------------------
 
# API key for currrency exchange.
API_KEY = "824498834668a752aad161e4"
 

base = input("Enter your base currency code: ").upper()
target = input("Enter your target currency code: ").upper()
 
amount = float(input("Enter amount: "))
 
 
try:
    # Url providing the currency rates of various countries
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
 
    response = requests.get(url) # send get request
    data = response.json() # converts response data into json format.

    exchange_rate = data['conversion_rates'][target]

    converted_amount = amount * exchange_rate
    print(converted_amount)      
 

except Exception as e:
    print("Enter valid currency code.", e)


 
    
    