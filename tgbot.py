import aiogram
from cfg import TGBOT_TOKEN
from get_weather import get_current_weather_forecast

bot = aiogram.Bot(TGBOT_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: aiogram.types.Message) -> None:
    '''Обработчик команд start и help'''
    await message.reply('Привет! Меня зовут Синоптик. Напиши мне название города, и я пришлю сводку погоды!')


@dp.message_handler()
async def handle_weather_command(message: aiogram.types.Message):
    '''Обработчик сообщения с запросом погоды'''
    await get_current_weather_forecast(message)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)