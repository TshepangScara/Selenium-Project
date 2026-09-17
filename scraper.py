from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://books.toscrape.com/"


def main():
    driver = webdriver.Chrome()
    try:
        driver.get(BASE_URL)
        print("Page title:", driver.title)

        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        print(f"Found {len(books)} books on this page\n")

        for book in books:
            title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
            print(f"- {title} | {price}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
