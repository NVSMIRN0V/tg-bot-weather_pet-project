import requests
import datetime
from cfg import TGBOT_TOKEN


def get_beautiful_cityname_str(city: str) -> str:
    ''' Функция формирует строку с названием города'''
    pass


def get_beautiful_weather_description_str(weather_description: str, sunrise: datetime.time, sunset: datetime.time) -> str:
    ''' Функция формирует строку с описанием погоды '''
    pass


def get_beautiful_temperature_str(temperature: float) -> str:
    ''' Функция формирует строку со значением температуры'''
    pass


def get_beautiful_humidity_str(humidity: float) -> str:
    ''' Функция формирует строку со значением влажности'''
    pass


def get_beautiful_pressure_str(pressure: float) -> str:
    ''' Функция формирует строку со значением давления'''
    pass


def get_beautiful_wind_description_str(wind_speed: float) -> str:
    ''' Функция формирует строку с данными о ветре'''
    pass


def get_beautiful_goodbye_message_str() -> str:
    ''' Функция формирует строку с обращением к пользователю'''
    pass


def get_beautiful_datetime_str() -> str:
    ''' Функция формирует строку со значениями даты и времени'''
    pass


def get_weather(city: str):
    # запрос
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TGBOT_TOKEN}&units=metric')
    response = request.json()

    # для проверки времени суток (get_beautiful_weather_description(arg, sunrise, sunset))
    sunrise = datetime.datetime.fromtimestamp(response['sys']['sunrise']).time()
    sunset = datetime.datetime.fromtimestamp(response['sys']['sunset']).time()

    # извлечение нужных данных из ответа на запрос
    city = response['name']
    weather_description = response['weather'][0]['main']
    humidity = response['main']['humidity']
    pressure = response['main']['pressure']
    wind_description = response['wind']['speed']
    goodbye_message = get_beautiful_goodbye_message_str()
    today = get_beautiful_datetime_str()

    # печать ответа пользователю
    print(city, weather_description, humidity)