import os

import requests

from playwright.sync_api import sync_playwright

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

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page(locale="ru-RU")

        page.goto(

            "https://bilet.railways.kz",

            wait_until="networkidle",

            timeout=60000

        )

        page.wait_for_timeout(3000)

        # показываем все видимые поля

        print("ВИДИМЫЕ INPUT:")

        inputs = page.locator("input:visible")

        print("Количество:", inputs.count())

        for i in range(inputs.count()):

            print(

                i,

                inputs.nth(i).get_attribute("placeholder"),

                inputs.nth(i).get_attribute("class")

            )

        browser.close()

        return False

send_message(

    "🚆 Мониторинг КТЖ запущен\n"

    "Поезд: 146\n"

    "Петропавловск → Астана Нурлы Жол\n"

    "Дата: 1 августа 2026"

)

if check_ticket():

    send_message(

        "🎫 Появился билет!\n"

        "Поезд: 146\n"

        "Петропавловск → Астана Нурлы Жол"

    )
