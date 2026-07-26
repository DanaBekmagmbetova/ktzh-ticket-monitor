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

        inputs = page.locator("input:visible")

        # Откуда

        inputs.nth(0).fill("Петропавловск")

        page.wait_for_timeout(1500)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Куда

        inputs.nth(1).fill("Астана Нурлы Жол")

        page.wait_for_timeout(1500)

        page.keyboard.press("ArrowDown")

        page.keyboard.press("Enter")

        # Дата

        inputs.nth(2).fill("01.08.2026")

        # Поиск

        page.get_by_text("Найти билеты").click()

        page.wait_for_timeout(10000)

        result = page.locator("body").inner_text()

        print(result[:5000])

        browser.close()

        # Если результатов нет

        if "Найдено результата - 0" in result:

            return False

        # Если появился поезд 146

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

            "Дата: 1 августа 2026"

        )

        save_status("found")

else:

    save_status("empty")
