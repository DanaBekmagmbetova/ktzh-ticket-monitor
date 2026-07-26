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

        browser = p.chromium.launch(

            headless=True

        )

        page = browser.new_page(

            locale="ru-RU"

        )

        page.goto(

            "https://bilet.railways.kz",

            wait_until="networkidle",

            timeout=60000

        )

        page.wait_for_timeout(3000)

        # Откуда

        departure = page.locator(

            'input[name="route_search_form[departureStation]"]'

        )

        departure.fill("Петропавловск")

        page.wait_for_timeout(2000)

        # выбираем подсказку

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Куда

        arrival = page.locator(

            'input[name="route_search_form[arrivalStation]"]'

        )

        arrival.fill("Астана Нурлы Жол")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Дата

        date = page.locator(

            'input[name="route_search_form[forwardDepartureDate]"]'

        )

        date.fill("01-08-2026")

        # Нажать поиск

        page.get_by_text("Билеттерді табыңыз").click()

        page.wait_for_timeout(10000)

        result = page.locator("body").inner_text()

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

        "🎫 Появился поезд 146!\n"

        "Петропавловск → Астана Нурлы Жол\n"

        "Дата: 1 августа 2026"

    )
