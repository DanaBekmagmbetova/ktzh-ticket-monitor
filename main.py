import os

import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]

CHAT_ID = "494750357"

def send_message(text):

    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"

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

    print("ОТВЕТ КТЖ:")

    print(response.text[:3000])

    return False

send_message(

    "🚆 Мониторинг билетов КТЖ запущен\n"

    "Поезд: 146\n"

    "Петропавловск → Астана Нурлы Жол\n"

    "Дата: 1 августа 2026"

)

check_ticket()
