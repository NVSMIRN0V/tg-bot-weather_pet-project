import requests
import datetime
from cfg import TGBOT_TOKEN


def get_beautiful_cityname_str(city: str) -> str:
    ''' Функция формирует строку с названием города'''
    result = '\U0001F3E1 Город: ' + city
    return result


def get_beautiful_weather_description_str(weather_description: str, sunrise: datetime.time, sunset: datetime.time) -> str:
    ''' Функция формирует строку с описанием погоды '''
    descriptions = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U0001F327',
        'Drizzle': 'Дождь \U0001F327',
        'Thunderstorm': 'Гроза \U000026C8',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B',
    }
    result = descriptions[weather_description] if weather_description in descriptions else 'Посмотрите в окно. Не пойму что там за погода!'
    result = '\U0001F31D Погода: ' + result if sunrise < datetime.datetime.now().time() < sunset else '\U0001F31A Погода: ' + result  
    return result


def get_beautiful_temperature_str(temperature: float) -> str:
    ''' Функция формирует строку со значением температуры'''
    result = '\U0001F321 Температура: ' + str(round(temperature, 1)) + '\U00002103'
    return result


def get_beautiful_humidity_str(humidity: float) -> str:
    ''' Функция формирует строку со значением влажности'''
    result = '\U0001F4A6 Влажность: ' + str(humidity) + '%'
    return result


def get_beautiful_pressure_str(pressure: float) -> str:
    ''' Функция формирует строку со значением давления'''
    pressure = round(pressure * 0.750063755419211, 2)
    result = '\U0001F4C8 Давление: ' + str(pressure) + ' мм.рт.ст.' if pressure > 760.00 else '\U0001F4C9 Давление: ' + str(pressure) + ' мм.рт.ст.'
    return result


def get_beautiful_wind_description_str(wind_speed: float) -> str:
    ''' Функция формирует строку с данными о ветре'''
    if  wind_speed >= 10.8:
        result = '\U0001F32C Ветер: ' + 'Сильный\U0001F32A, ' + str(wind_speed) + ' м/с'
    elif 5.5 < wind_speed < 10.8:
        result = '\U0001F32C Ветер: ' + 'Умеренный\U0001F32A, ' + str(wind_speed) + ' м/с'
    elif  0.3 < wind_speed < 5.5:
        result = '\U0001F32C Ветер: ' + 'Слабый\U0001F32A, ' + str(wind_speed) + ' м/с'
    else:
        result = '\U0001F32C Ветер: ' + 'Штиль\U0001F32A'
    return result


def get_beautiful_goodbye_message_str() -> str:
    ''' Функция формирует строку с обращением к пользователю'''
    result = '\nСпасибо за обращение!\U0001F44B'
    return result


def get_beautiful_datetime_str() -> str:
    ''' Функция формирует строку со значениями даты и времени'''
    today = datetime.datetime.now()
    time = today.time().strftime('%H:%M')
    date = today.date().strftime('%d/%m/%y')
    result = '\U0001F4C5 Дата: ' + date + '\n' + '\U0001F557 Время: ' + time 
    return result


def get_weather(city: str):
    # запрос
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TGBOT_TOKEN}&units=metric')
    response = request.json()

    # для проверки времени суток (get_beautiful_weather_description(arg, sunrise, sunset))
    sunrise = datetime.datetime.fromtimestamp(response['sys']['sunrise']).time()
    sunset = datetime.datetime.fromtimestamp(response['sys']['sunset']).time()

    # извлечение нужных данных из ответа на запрос
    city = get_beautiful_cityname_str(response['name'])
    weather_description = get_beautiful_weather_description_str(response['weather'][0]['main'], sunrise, sunset)
    temperature = get_beautiful_temperature_str(response['main']['temp'])
    humidity = get_beautiful_humidity_str(response['main']['humidity'])
    pressure = get_beautiful_pressure_str(response['main']['pressure'])
    wind_description = get_beautiful_wind_description_str(response['wind']['speed'])
    goodbye_message = get_beautiful_goodbye_message_str()
    today = get_beautiful_datetime_str()

    # печать ответа пользователю
    print(city, weather_description, humidity)
