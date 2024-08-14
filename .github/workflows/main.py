import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = '7277680211:AAHcDhYtpKRUba2kg6XpUgIGQhYcC_6bgss'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспатчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(content_types=['text'])
async def delete_message_if_not_allowed(message: types.Message):
    # Проверяем, содержит ли сообщение нужные слова
    if not ('гарант' in message.text.lower() or 'weargon' in message.text.lower()):
        await message.delete()  # Удаляем сообщение
        logging.info(f"Удалено сообщение от {message.from_user.username}: {message.text}")

        # Отправляем уведомление в тот же чат
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                f"{message.from_user.username}, ваше сообщение было удалено. "
                "Добавьте в свое сообщение: 'гарант @Weargon' и тогда сообщение будет отправлено в чат!"
            )
        )

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
