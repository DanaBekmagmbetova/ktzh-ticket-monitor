import os

import requests

import time

BOT_TOKEN = os.environ["BOT_TOKEN"]

CHAT_ID = "494750357"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(

        url,

        data={

            "chat_id": CHAT_ID,

            "text": text

        }

    )

def check_ticket():

    url = "https://bilet.railways.kz/sale/default/car/search"

    params = {

        "car_search_form[departureStation]": "2040500",

        "car_search_form[arrivalStation]": "2708001",

        "car_search_form[forwardDirection][departureTime]": "2026-08-01T00:00:00",

        "car_search_form[forwardDirection][train]": "146",

        "car_search_form[forwardDirection][isObligativeElReg]": "0"

    }

    response = requests.get(url, params=params)

    if "146" in response.text:

        return True

    return False

send_message(

    "🚆 Мониторинг билетов КТЖ запущен\n"

    "Поезд: 146\n"

    "Петропавловск → Астана Нурлы Жол\n"

    "Дата: 1 августа 2026"

)

while True:

    try:

        if check_ticket():

            send_message(

                "🎫 Появился билет!\n"

                "Поезд: 146\n"

                "Петропавловск → Астана Нурлы Жол\n"

                "Дата: 1 августа 2026"

            )

            break

        time.sleep(300)

    except Exception as e:

        send_message(f"Ошибка: {e}")

        time.sleep(300)
