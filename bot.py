import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackContext,
)
import re
import requests

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния для ConversationHandler
NAME, PHONE, MENU = range(3)

# Хранилище данных пользователей (временно, можно заменить на базу данных)
user_data = {}

# URL стороннего сервиса для генерации QR-кода
QR_SERVICE_URL = "http://localhost:5000/generate_qr"  # Замените на реальный URL


async def start(update: Update, context: CallbackContext) -> int:
    """Приветствие пользователя и предложение оформить карту."""
    reply_keyboard = [["Да, хочу карту!", "Нет, спасибо"]]
    await update.message.reply_text(
        "Здравствуйте! Добро пожаловать в программу лояльности (Хлебная пекарня)! "
        "Станьте участником нашего клуба и получайте эксклюзивные предложения и бонусы. "
        "Хотите оформить клубную карту?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return NAME


async def cancel(update: Update, context: CallbackContext) -> int:
    """Обработка отказа от оформления карты."""
    await update.message.reply_text(
        "Спасибо за внимание! Если передумаете, всегда можете начать снова командой /start.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


async def get_name(update: Update, context: CallbackContext) -> int:
    """Получение ФИО пользователя."""
    user_response = update.message.text
    if user_response == "Нет, спасибо":
        return await cancel(update, context)

    context.user_data["choice"] = "card"
    await update.message.reply_text(
        "Отлично! Пожалуйста, введите ваше ФИО:", reply_markup=ReplyKeyboardRemove()
    )
    return PHONE


async def get_phone(update: Update, context: CallbackContext) -> int:
    """Получение номера телефона пользователя с проверкой формата."""
    user_name = update.message.text
    context.user_data["name"] = user_name

    await update.message.reply_text(
        "Теперь введите ваш номер телефона в формате +79XXXXXXXXX:"
    )
    return MENU


async def validate_phone(update: Update, context: CallbackContext) -> int:
    """Валидация номера телефона и создание QR-кода."""
    phone = update.message.text
    phone_pattern = r"^\+79\d{9}$"

    if not re.match(phone_pattern, phone):
        await update.message.reply_text(
            "Пожалуйста, введите номер телефона в правильном формате: +79XXXXXXXXX"
        )
        return PHONE

    context.user_data["phone"] = phone

    # Генерация QR-кода через сторонний сервис
    try:
        response = requests.post(QR_SERVICE_URL, json={"phone": phone})
        response.raise_for_status()
        qr_code_url = response.json().get("qr_code_url")
        user_id = update.effective_user.id
        user_data[user_id] = {"qr_code_url": qr_code_url}
    except Exception as e:
        logger.error(f"Ошибка при генерации QR-кода: {e}")
        await update.message.reply_text(
            "Произошла ошибка при создании карты. Попробуйте позже."
        )
        return ConversationHandler.END

    # Отправка сообщения об успешной регистрации
    reply_keyboard = [["Моя карта", "Узнать больше"]]
    await update.message.reply_text(
        "Поздравляем! Ваша клубная карта успешно оформлена! Вам начислено 300 бонусов.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return MENU


async def show_card(update: Update, context: CallbackContext) -> int:
    """Показывает QR-код пользователя."""
    user_id = update.effective_user.id
    user_info = user_data.get(user_id)

    if not user_info or "qr_code_url" not in user_info:
        await update.message.reply_text(
            "Кажется, у вас еще нет клубной карты. Начните с команды /start."
        )
        return ConversationHandler.END

    qr_code_url = user_info["qr_code_url"]
    await update.message.reply_photo(
        photo=qr_code_url, caption="Ваша клубная карта:"
    )
    return MENU


async def more_info(update: Update, context: CallbackContext) -> int:
    """Показывает дополнительную информацию."""
    await update.message.reply_text(
        "Здесь будет информация о программе лояльности и акциях. "
        "Следите за обновлениями!"
    )
    return MENU


async def broadcast(update: Update, context: CallbackContext) -> None:
    """Рассылка сообщений всем пользователям (команда для модератора)."""
    if update.effective_user.id != MODERATOR_ID:  # Замените на ID модератора
        await update.message.reply_text("У вас нет прав для выполнения этой команды.")
        return

    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("Пожалуйста, укажите текст для рассылки.")
        return

    for user_id in user_data.keys():
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            logger.error(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

    await update.message.reply_text("Рассылка завершена.")


def main() -> None:
    """Запуск бота."""
    application = Application.builder().token("444444444444").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            MENU: [
                MessageHandler(filters.Regex("^Моя карта$"), show_card),
                MessageHandler(filters.Regex("^Узнать больше$"), more_info),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("broadcast", broadcast))

    application.run_polling()


if __name__ == "__main__":
    main()
