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

        # Откуда

        inputs = page.locator("input:visible")

        departure = inputs.nth(0)

        arrival = inputs.nth(1)

        departure.fill("Петропавловск")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        arrival.fill("Астана Нурлы Жол")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Дата

        date = inputs.nth(2)

        date.fill("01.08.2026")

        # Нажимаем кнопку поиска

        page.get_by_text("Билеттерді табыңыз").click()

        page.wait_for_timeout(10000)

        result = page.locator("body").inner_text()

        print("РЕЗУЛЬТАТ ПОИСКА:")

        print(result[:5000])

        browser.close()

        if "146" in result:

            return True

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

        "Петропавловск → Астана Нурлы Жол\n"

        "Дата: 1 августа 2026"

    )
