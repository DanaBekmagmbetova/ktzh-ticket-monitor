import requests

import time

from datetime import datetime

BOT_TOKEN = "8791960531:AAHovdmQzeZyQZM5E02P_e17Ay3WE5J4prc"

CHAT_ID = "494750357"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={

        "chat_id": CHAT_ID,

        "text": text

    })

def check_ticket():

    # Пока тестовая проверка

    # сюда дальше подключим проверку КТЖ

    return False

send_message("🚆 Мониторинг билетов КТЖ запущен\nПоезд: 146Н\nПетропавловск → Астана\nДата: 1 августа")

while True:

    try:

        if check_ticket():

            send_message(

                "🎫 Появился билет!\n"

                "Поезд: 146\n"

                "Петропавловск → Астана\n"

                "Дата: 1 августа"

            )

            break

        time.sleep(300)  # проверка каждые 5 минут

    except Exception as e:

        send_message(f"Ошибка мониторинга: {e}")

        time.sleep(300)
