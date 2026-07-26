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

        # Видимые поля

        inputs = page.locator("input:visible")

        # Откуда

        departure = inputs.nth(0)

        departure.fill("Петропавловск")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Куда

        arrival = inputs.nth(1)

        arrival.fill("Астана Нурлы Жол")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Дата

        date = inputs.nth(2)

        date.fill("01.08.2026")

        page.wait_for_timeout(1000)

        # Поиск

        page.locator("button").filter(

            has_text="Билеттер"

        ).click()

        page.wait_for_timeout(10000)

        result = page.locator("body").inner_text()

        print("РЕЗУЛЬТАТ ПОИСКА:")

        print(result[:5000])

        browser.close()

        # Билетов нет

        if "Поиск не дал результатов" in result:

            return False

        if "Найдено результата - 0" in result:

            return False

        # Поезд появился

        if "146" in result:

            return True

        return False

def get_old_status():

    try:

        with open("status.txt", "r") as f:

            return f.read()

    except:

        return "none"

def save_status(status):

    with open("status.txt", "w") as f:

        f.write(status)

# Проверка

ticket = check_ticket()

old_status = get_old_status()

if ticket:

    if old_status != "found":

        send_message(

            "🎫 Появился билет!\n\n"

            "🚆 Поезд: 146\n"

            "Маршрут: Петропавловск → Астана Нурлы Жол\n"

            "📅 Дата: 1 августа 2026"

        )

        save_status("found")

else:

    save_status("empty")
