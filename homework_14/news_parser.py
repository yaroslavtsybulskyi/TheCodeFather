"""
Module: news_parser
-------------------
This script fetches news from a website, processes it,
and provides statistical insights such as the number of news articles per hour.
"""

import csv
import logging
import os
from dataclasses import dataclass

from typing import Optional, List, Dict
from datetime import datetime, timedelta

import requests
import pandas as pd
from bs4 import BeautifulSoup
import pytz

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


@dataclass
class NewsArticle:
    """
    Data class to store news article information.
    """

    title: str
    link: str
    date: str
    summary: str

    def __str__(self) -> str:
        return f"{self.title} {self.date} {self.summary} {self.link}"


def get_page(url: str) -> Optional[BeautifulSoup]:
    """
    Fetches the HTML content of a given URL and returns a BeautifulSoup object.
    :param url: The URL of the webpage to fetch.
    :return: A BeautifulSoup object containing the parsed HTML, or None if an error occurs.
    :raises TypeError: If the provided URL is not a string.
    """
    if not isinstance(url, str):
        raise TypeError('URL must be a string')
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except requests.exceptions.RequestException as e:
        error_type = type(e).__name__
        logger.error("%s while fetching %s: %s", error_type, url, e)
    return None


def parse_news(soap: BeautifulSoup) -> List[NewsArticle]:
    """
    Parses news articles from the BeautifulSoup object.

    :param soap: A BeautifulSoup object of the webpage.
    :return: A list of news articles containing news details (title, link, date, summary).
    :raises TypeError: If the provided BeautifulSoup object is not a BeautifulSoup object.
    """
    if not isinstance(soap, BeautifulSoup):
        raise TypeError('Soap must be a BeautifulSoup object')

    news_list: List[NewsArticle] = []
    try:
        news_items = soap.find_all("a", class_="fua-news-feed__item")

        for item in news_items:
            title_tag = item.find("span", {"data-vr-headline": True})
            title = title_tag.text.strip() if title_tag else ""
            link = item.get("href", "")

            time_tag = item.find("time", class_="fua-news-feed__time")
            date = time_tag["datetime"] if time_tag and "datetime" in time_tag.attrs else ""

            summary = item["data-vr-contentbox"] if "data-vr-contentbox" in item.attrs else ""

            news_article = NewsArticle(title=title, link=link, date=date, summary=summary)
            news_list.append(news_article)
    except AttributeError as e:
        logger.error("Attribute Error while fetching news items: %s", e)
    except TypeError as e:
        logger.error("Type Error while fetching news items: %s", e)
    except Exception as e:
        logger.error("Unknown error while fetching news items: %s", e)

    return news_list


def save_to_csv(data: List[NewsArticle], filename: str = "news.csv") -> None:
    """
    Saves news data to a CSV file.

    :param data: List of news articles to save.
    :param filename: The name of the CSV file (default: "news.csv").

    :raises TypeError: If the provided data is not a list.
    :raises ValueError: If the provided data is not a list of dictionaries.
    """
    if not isinstance(data, list):
        raise TypeError('Data must be a list of news articles.')

    if not isinstance(filename, str):
        raise TypeError('Filename must be a string')

    if not filename.endswith(".csv"):
        raise ValueError('Filename must end with ".csv"')

    if not data:
        logger.error("No news data to save. The file will not be created.")
        return None
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'link', 'date', 'summary'])
            writer.writeheader()
            for news_article in data:
                writer.writerow({
                    'title': news_article.title,
                    'link': news_article.link,
                    'date': news_article.date,
                    'summary': news_article.summary
                })
            logger.info("Successfully saved news data to %s", filename)
    except PermissionError as e:
        logger.error("Permission Error while saving data to CSV file: %s", e)
    except IOError as e:
        logger.error("Error while saving news data to file: %s", e)
    except KeyError as e:
        logger.error("Key Error: %s", e)
    except Exception as e:
        logger.error("Unexpected error while saving CSV: %s", e)
    return None


def open_csv(csvfile: str) -> Optional[pd.DataFrame]:
    """
     Opens a CSV file and returns it as a pandas DataFrame.

    :param csvfile: The path to the CSV file.
    :return: A pandas DataFrame containing the CSV data.
    :raises FileNotFoundError: If the file does not exist.
    """
    if not isinstance(csvfile, str):
        raise TypeError('CSV file must be a string')
    if not csvfile.endswith(".csv"):
        raise ValueError('CSV file must end with ".csv"')
    if not os.path.exists(csvfile):
        logger.error("File %s does not exist", csvfile)

    try:
        df = pd.read_csv(csvfile)
        df['date'] = pd.to_datetime(df['date'])

        df.dropna(subset=['date'], inplace=True)
        return df
    except Exception as e:
        logger.error("Unexpected error while opening %s: %s", csvfile, e)


def filter_by_hours(csvfile: str, hours: int) -> Optional[List[NewsArticle]]:
    """
    Filters news articles from the CSV file based on the given number of hours.

    :param csvfile: The path to the CSV file.
    :param hours: Number of hours to filter from the current time.
    :return: A list of dictionaries with filtered news articles.
    :raise TypeError: If the provided hours is not an integer.
    :raises ValueError: If the provided hours is not an integer or less than 0 or greater than 24.
    """
    if not isinstance(hours, int):
        raise TypeError('Number of hours must be an integer')
    if hours <= 0 or hours > 24:
        raise ValueError('Number of hours must be positive and be less than 24')
    try:
        df = open_csv(csvfile)
        if df is None or df.empty:
            logger.error("No data in the csv")
            return []

        now_utc = datetime.now(pytz.timezone('Europe/Kiev'))
        filtered_df = df[df['date'] >= now_utc - timedelta(hours=hours)]

        filtered_news: List[NewsArticle] = [
            NewsArticle(title=row['title'], link=row['link'], date=str(row['date']), summary=row['summary'])
            for index, row in filtered_df.iterrows()
        ]
        return filtered_news
    except Exception as e:
        logger.error("Unexpected error while filtering news articles: %s", e)


def stats(csvfile: str) -> None:
    """
    Generates and displays statistics about news articles.
    :param csvfile: The path to the CSV file.
    :return: None
    """
    df = open_csv(csvfile)
    if df is None or df.empty:
        logging.error("No data in the csv")
        return None
    try:
        news_per_hour = df.groupby(df['date'].dt.hour).size()

        news_stats = news_per_hour.to_dict()
        print('News by hours:')
        for hour, count in news_stats.items():
            print(f"{hour:02d}   | {count}")

        earliest = df['date'].min()
        latest = df['date'].max()
        total_articles = len(df)
        print(f"Total number of articles: {total_articles}")
        print(f"Earliest news article: {earliest}")
        print(f"Latest news article: {latest}")
    except Exception as e:
        logger.error("Error generating statistics: %s", e)


if __name__ == '__main__':
    soup = get_page('https://finance.ua/')
    if soup:
        news = parse_news(soup)
        if news:
            save_to_csv(news)
            filtered_news = filter_by_hours('news.csv', 5)
            if filtered_news:
                for news in filtered_news:
                    print(news)
            stats('news.csv')
