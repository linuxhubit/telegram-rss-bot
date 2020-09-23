# Based on:
# https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd

from datetime import timedelta, datetime
from time import sleep
import urllib.parse

import feedparser
import requests
from dateutil import parser

import config


def send_message(message):
    message = urllib.parse.quote(message)
    query = f'https://api.telegram.org/bot{config.Bot.token}/sendMessage?chat_id={config.Channel.id}&text={message}'
    requests.get(query)


def main():
    print("Starting Teelgram RSS bot..")

    for feed in config.Feeds.urls:
        feed = feedparser.parse(feed)
        for entry in feed.entries:

            parsed_date = parser.parse(entry.published)
            parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None)
            now_date = datetime.utcnow()

            post = "💬 {0}\n{1}".format(
                entry.title,
                entry.links[0].href
            )

            published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
            if published_20_minutes_ago:
                send_message(post)


if __name__ == "__main__":
    while True:
        main()
        sleep(20 * 60)
