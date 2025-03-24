# 🍞 Telegram-бот программы лояльности "Хлебная пекарня"

## 📝 Описание проекта
Этот Telegram-бот позволяет пользователям оформить клубную карту лояльности, получать бонусы и участвовать в акциях.  
Бот использует \`ConversationHandler\` для управления диалогом с пользователем, а также интегрируется с внешним сервисом для генерации QR-кодов.

---

## 🛠 Требования к установке
1. Python 3.7 или выше.
2. Установите библиотеку \`python-telegram-bot\`:  
   \`\`\`bash
   pip install python-telegram-bot --upgrade
   \`\`\`
3. Установите библиотеку \`requests\`:  
   \`\`\`bash
   pip install requests
   \`\`\`
4. Доступ к внешнему сервису для генерации QR-кода (URL настраивается в коде).

---

## 🚀 Запуск бота
1. Создайте файл \`.env\` в корне проекта и добавьте следующие переменные:
   \`\`\`bash
   TELEGRAM_BOT_TOKEN=ваш_токен_бота
   QR_SERVICE_URL=http://localhost:5000/generate_qr
   MODERATOR_ID=ID_модератора
   \`\`\`
2. Установите зависимости:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Запустите бота:
   \`\`\`bash
   python bot.py
   \`\`\`

---

## ⚙️ Функционал бота
- \`/start\` - Начало диалога с пользователем.
- Ввод ФИО и номера телефона в формате \`+79XXXXXXXXX\`.
- После успешной регистрации бот отправляет QR-код клубной карты.
- Меню пользователя:
  - \`Моя карта\` - Показывает QR-код.
  - \`Узнать больше\` - Информация о программе лояльности.
- \`/broadcast текст\` - Отправка сообщения всем зарегистрированным пользователям (для модератора).

---

## 📊 Логирование
Логи сохраняются в консоль в формате:
\`\`\`
%(asctime)s - %(name)s - %(levelname)s - %(message)s
\`\`\`

---

## ❗ Возможные ошибки
1. **Ошибка подключения к сервису QR-кодов**  
   Проверьте доступность URL в переменной \`QR_SERVICE_URL\`.
2. **Проблемы с токеном Telegram**  
   Убедитесь, что \`TELEGRAM_BOT_TOKEN\` указан правильно.
3. **Неверный формат номера телефона**  
   Бот запросит повторный ввод, если формат неверный.

---

## 📜 Лицензия
Этот проект распространяется под лицензией [MIT](LICENSE).

---

## 👥 Авторы
Разработано командой **Хлебная пекарня**.

---

## 📩 Поддержка
Для вопросов и предложений пишите на [saturn4ik@mail.ru](mailto:saturn4ik@mail.ru).
