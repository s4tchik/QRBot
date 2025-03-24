#!/bin/bash

# Цвета для оформления
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Заголовок
echo -e "${BLUE}README для Telegram-бота программы лояльности \"Хлебная пекарня\"${NC}"

# Описание проекта
echo -e "\n${GREEN}Описание проекта${NC}"
echo "Этот Telegram-бот позволяет пользователям оформить клубную карту лояльности,"
echo "получать бонусы и участвовать в акциях. Бот использует ${YELLOW}ConversationHandler${NC}"
echo "для управления диалогом с пользователем, а также интегрируется с внешним сервисом"
echo "для генерации QR-кодов."

# Требования к установке
echo -e "\n${GREEN}Требования к установке${NC}"
echo "1. Python 3.7 или выше"
echo "2. Установите библиотеку python-telegram-bot: ${YELLOW}pip install python-telegram-bot --upgrade${NC}"
echo "3. Установите библиотеку requests: ${YELLOW}pip install requests${NC}"
echo "4. Доступ к внешнему сервису для генерации QR-кода (URL настраивается в коде)."

# Установка зависимостей
echo -e "\n${GREEN}Установка зависимостей${NC}"
echo "Выполните команду для установки зависимостей:"
echo -e "${YELLOW}pip install -r requirements.txt${NC}"

# Настройка переменных окружения
echo -e "\n${GREEN}Настройка переменных окружения${NC}"
echo "Создайте файл .env в корне проекта и добавьте следующие переменные:"
echo -e "${YELLOW}TELEGRAM_BOT_TOKEN=ваш_токен_бота${NC}"
echo -e "${YELLOW}QR_SERVICE_URL=http://localhost:5000/generate_qr${NC}"
echo -e "${YELLOW}MODERATOR_ID=ID_модератора${NC}"

# Запуск бота
echo -e "\n${GREEN}Запуск бота${NC}"
echo "Для запуска бота выполните команду:"
echo -e "${YELLOW}python bot.py${NC}"

# Функционал бота
echo -e "\n${GREEN}Функционал бота${NC}"
echo -e "1. ${YELLOW}/start${NC} - Начало диалога с пользователем."
echo -e "2. Ввод ФИО и номера телефона в формате ${YELLOW}+79XXXXXXXXX${NC}."
echo -e "3. После успешной регистрации бот отправляет QR-код клубной карты."
echo -e "4. Меню пользователя:"
echo -e "   - ${YELLOW}Моя карта${NC} - Показывает QR-код."
echo -e "   - ${YELLOW}Узнать больше${NC} - Информация о программе лояльности."
echo -e "5. ${YELLOW}/broadcast текст${NC} - Отправка сообщения всем зарегистрированным пользователям (для модератора)."

# Логирование
echo -e "\n${GREEN}Логирование${NC}"
echo "Логи сохраняются в консоль в формате:"
echo -e "${YELLOW}%(asctime)s - %(name)s - %(levelname)s - %(message)s${NC}"

# Возможные ошибки
echo -e "\n${GREEN}Возможные ошибки${NC}"
echo -e "1. ${RED}Ошибка подключения к сервису QR-кодов${NC}"
echo "   Проверьте доступность URL в переменной ${YELLOW}QR_SERVICE_URL${NC}."
echo -e "2. ${RED}Проблемы с токеном Telegram${NC}"
echo "   Убедитесь, что ${YELLOW}TELEGRAM_BOT_TOKEN${NC} указан правильно."
echo -e "3. ${RED}Неверный формат номера телефона${NC}"
echo "   Бот запросит повторный ввод, если формат неверный."

# Лицензия
echo -e "\n${GREEN}Лицензия${NC}"
echo "Этот проект распространяется под лицензией ${YELLOW}MIT${NC}."

# Авторы
echo -e "\n${GREEN}Авторы${NC}"
echo "Разработано командой ${YELLOW}Хлебная пекарня${NC}."

# Поддержка
echo -e "\n${GREEN}Поддержка${NC}"
echo "Для вопросов и предложений пишите на ${YELLOW}saturn4ik@mail.ru${NC}."
