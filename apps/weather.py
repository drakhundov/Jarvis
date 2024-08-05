import requests

API = '00696acde78611693923f3fff2f8ed11'
URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + API


def weather(place):
    info = requests.get(URL.format(city=place)).json()

    status = 'It is ' + info['weather'][0]['description'] + ' in ' + place + ' now. '
    status += 'Temperature now is ' + str(info['main']['temp']) + ' degrees.'

    return status