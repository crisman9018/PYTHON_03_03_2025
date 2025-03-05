import requests
import json
pagina = "https://api.openweathermap.org/data/2.5/weather?q=Piedecuesta,co&APPID=4491ad6d8e5c821739cbd71c337ec5c2&units=metric"
page = requests.get(str(pagina))
json_data = json.loads(page.text)
print(json_data["main"]["temp"])
print(json_data["weather"][0]["main"])
print(json_data["weather"][0]["description"])