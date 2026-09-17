import argparse
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"


def main():
    parser = argparse.ArgumentParser(description="Scrape book titles and prices.")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="run Chrome without opening a visible window",
    )
    args = parser.parse_args()

    options = Options()
    if args.headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(BASE_URL)
        print("Page title:", driver.title)

        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "price"])

            page_num = 1
            while True:
                print(f"\n--- Page {page_num} ---")
                books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
                print(f"Found {len(books)} books on this page\n")

                for book in books:
                    title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
                    price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
                    print(f"- {title} | {price}")
                    writer.writerow([title, price])

                try:
                    next_link = driver.find_element(By.CSS_SELECTOR, "li.next a")
                except NoSuchElementException:
                    break

                next_link.click()
                page_num += 1

        print(f"\nSaved results to {OUTPUT_FILE}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
