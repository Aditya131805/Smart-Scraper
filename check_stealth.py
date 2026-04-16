from playwright.sync_api import sync_playwright
import time
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def check_stealth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    args=[
                                        "--disable-blink-features=AutomationControlled",
                                        "--use-gl=desktop"
                                    ])

        context = browser.new_context(
            user_agent=random.choice(USER_AGENTS),
            viewport={"width": 1280, "height": 800},
            locale="en-US",
            timezone_id="Asia/Kolkata"
        )

        page = context.new_page()
        page.goto("https://bot.sannysoft.com/")
        time.sleep(5)
        page.screenshot(path="stealth_check.png")
        browser.close()

check_stealth()