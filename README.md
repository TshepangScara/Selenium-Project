# Selenium Book Scraper

A Python + Selenium web scraper that crawls every page of [books.toscrape.com](https://books.toscrape.com/) (a site built for scraping practice) and exports each book's title and price to a CSV file.

## What it demonstrates

- Browser automation with Selenium WebDriver
- Locating elements with CSS selectors (`find_element` / `find_elements`)
- Pagination handling — following "next page" links until none remain
- Exception handling (`NoSuchElementException` to detect the last page)
- Structured data export to CSV with correct UTF-8 encoding

## Requirements

- Python 3
- Google Chrome installed

## Setup

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Usage

```bash
python scraper.py
```

This opens a Chrome window, scrapes all 50 pages (1000 books), prints progress to the console, and writes the results to `books.csv` (title, price) in the project root.

## Project structure

```
scraper.py          # main scraper script
requirements.txt     # pinned dependencies
```
