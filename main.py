from playwright.sync_api import sync_playwright
import time
import random
import pandas as pd

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# proxies = [
#     "http://username:password@proxy1:port",
#     "http://username:password@proxy2:port",
#     "http://username:password@proxy3:port"
# ]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def scraper(page):
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector(".product_pod")

    books_data = []
    books = page.query_selector_all(".product_pod")

    for book in books:
        try:
            title = book.query_selector("h3 a").get_attribute("title")

            price = float(
                book.query_selector(".price_color")
                .inner_text()
                .strip()
                .replace("£", "")
            )

            rating = RATING_MAP.get(
                book.query_selector(".star-rating")
                .get_attribute("class")
                .split()[-1]
            )

            books_data.append((title, price, rating))

        except Exception:
            continue

    return books_data


def main():
    all_books = []

    with sync_playwright() as p:
        # selected_proxy=random.choice(proxies)
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--use-gl=desktop"
            ]
        )

        context = browser.new_context(
            # proxy={
            #     "server": slected_proxy,"
            # }, better to keep changing proxy for each session to avoid detection
            user_agent=random.choice(USER_AGENTS),
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
            timezone_id="Asia/Kolkata"
        )

        page = context.new_page()

        page.goto("https://books.toscrape.com/catalogue/page-1.html")

        while True:
            books = None
            for attempt in range(3):
                try:
                    books = scraper(page)
                    break
                except Exception as e:
                    print(f"Retry {attempt+1}: {e}")
                    time.sleep(2)

            if books is None:
                print("Skipping page after retries.")
                break

            all_books.extend(books)
            print(f"Total books scraped: {len(all_books)}")

            page.mouse.wheel(0, random.randint(1000, 2000))

            next_button = page.query_selector(".next a")

            if next_button:
                current_url = page.url

                time.sleep(random.uniform(1, 3))
                next_button.click()

                page.wait_for_load_state("networkidle")

                if page.url == current_url:
                    print("Same page detected. Stopping.")
                    break
            else:
                print("No next page. Stopping.")
                break

        browser.close()

    return all_books


# Run scraper
data = main()

# Save to CSV
df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])
df.to_csv("books.csv", index=False)

print("Data saved to books.csv")