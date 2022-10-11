import requests
city = "Moscow,RU"
appid = "6d3f8d31864af7011ca72d6c02f1a8a5"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print('Прогноз погоды на сегодня:')
print("Город:", city, "\r\nСкорость ветра <", data['wind']['speed'], "> \r\nВидимость <",data['visibility'], ">")
print('')

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'], "> \r\nВидимость <",i['visibility'], ">")
    print("____________________________")