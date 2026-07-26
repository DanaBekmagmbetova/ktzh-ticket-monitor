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

    url = "https://bilet.railways.kz/sale/default/route/search"

    params = {

        "route_search_form[departureStation]": "2040500",

        "route_search_form[arrivalStation]": "2708001",

        "route_search_form[forwardDepartureDate]": "01-08-2026"

    }

    response = requests.get(url, params=params)

    print(response.text[:3000])

    if "146" in response.text:

        return True

    return False

send_message(

    "🚆 Мониторинг билетов КТЖ запущен\n"

    "Поезд: 146\n"

    "Петропавловск → Астана Нурлы Жол\n"

    "Дата: 1 августа 2026"

)

check_ticket()
