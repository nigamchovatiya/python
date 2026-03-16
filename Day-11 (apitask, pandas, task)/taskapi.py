""" 
here i fetch a free weather api data,
and print here.

"""

# ---------------------------------------------------

import requests

# ---------------------------------------------------

# api key for a weather
API_KEY = "720e720bfdbe191f1d37cb9d9f099f11"

city = "ahmedabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"



try:
    # send get request
    response = requests.get(url)

    # convert respnose json
    data = response.json()

    # extract weather details
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # display data
    print(f"city: {city}")
    print(f"temperature: {temperature}")
    print(f"description: {description}")


except Exception as e:
    print("Error in fetch data:", e)    
