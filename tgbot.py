import aiogram
from cfg import TGBOT_TOKEN

bot = aiogram.Bot(TGBOT_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: aiogram.types.Message) -> None:
    '''Обработчик команд start и help'''
    await message.reply('Привет! Меня зовут Синоптик. Напиши мне название города, и я пришлю сводку погоды!')


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)