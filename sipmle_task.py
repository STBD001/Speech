import webbrowser
import requests

def open_website(url):
    webbrowser.open(url)

def get_weather(city):
    api_key = "8e7735c4e1ca01cab8259ab442bab77a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pl&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        weather_info = f"Aktualna temperatura w {city} to {temp} stopni Celsjusza. Pogoda: {description}."
        return weather_info
    else:
        return "Nie udało się pobrać prognozy pogody"