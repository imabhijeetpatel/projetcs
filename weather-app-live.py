# This is the live weather API app show Esential weather information of any City
''' The given API is my API so please use your own. visit =https://home.openweathermap.org/api_keys
 make your account and get your API'''

# Requirement for this app
# > pip install requests

import requests

API_KEY = "f9535b8b309aee9b8f5c943369c31d232004"
city = "Sagar"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appi=d{API_KEY}"
response= requests.get(url)

if response.status_code == 200:
    weather_data =response.json()
    print(weather_data)
else:
    print("An error raised: status code >", response.status_code)

API_KEY = "key"
BASE_URL = "URl"

# get weather data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response =requests.get(url)
        if response.status_code ==200:
            data =response.json()
            weather = {
                "city": data["name"],
                "Temprature":f"{data['main']['temp']}C",
                "weather": data['weather'][0]['description'].title(),
                "Humidity":f"{['main']['humidity']}%",
                "wind speed": f"{data['wind']['speed']}m/s"           
            }
            return weather
        elif response.status_code == 404:
            print("city not found")
        else:
            print("An error raised: status code >", response.status_code)
    except Exception as e:
        print("An error raised:", e)
    return None

# In this display the weather information
def display_weather(weather):
    print("\n--- Weather Information ---")
    for key,value in weather.items():
        print(f"{key}: {value}")

# In this step main progress loop
while True:
    print("\n---Weather App---")
    city = input("Enter a city name (or 'q' to quit):").strip()
    if city.lower() == 'q':
        break
    weather= get_weather(city)
    if weather:
         display_weather(weather)

