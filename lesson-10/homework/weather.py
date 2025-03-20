import requests

API_KEY = "i'could nit get my api key"  
CITY = "Tashkent"  

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc.capitalize()}")
    else:
        print("Oops! Couldn't get the weather. Check your API key or city name.")

get_weather(CITY)
