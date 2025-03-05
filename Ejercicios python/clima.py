import requests
import json
pagina = "https://api.openweathermap.org/data/2.5/weather?q=Piedecuesta,co&APPID=44ccd6fe4d5fe940989adbc892e28c5e&units=metric"
page = requests.get(str(pagina))
json_data = json.loads(page.text)
print(json_data)
print(json_data["main"]["temp"])
print(json_data["weather"][0]["main"])
print(json_data["weather"][0]["description"])