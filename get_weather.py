import requests

from cfg import TGBOT_TOKEN

def get_weather(city: str):
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TGBOT_TOKEN}&units=metric')
    response = request.json()

    city = response['name']
    print(city)


get_weather('Москва')
