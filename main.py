import requests

import time

from datetime import datetime

import os

BOT_TOKEN = os.environ["BOT_TOKEN"]

CHAT_ID = "494750357"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={

        "chat_id": CHAT_ID,

        "text": text

    })

def check_ticket():

    url = "https://bilet.railways.kz/sale/default/car/search"

    params = {

        "car_search_form[departureStation]": "2040500",

        "car_search_form[arrivalStation]": "2708001",

        "car_search_form[forwardDirection][departureTime]": "2026-08-01T00:00:00",

        "car_search_form[forwardDirection][fluentDeparture]": "",

        "car_search_form[forwardDirection][train]": "146",

        "car_search_form[forwardDirection][isObligativeElReg]": "0"

    }

    response = requests.get(url, params=params)

    text = response.text

    if "146" in text:

        return True

    return False

send_message("🚆 Мониторинг билетов КТЖ запущен\nПоезд: 146\nПетропавловск → Астана\nДата: 1 августа")

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
