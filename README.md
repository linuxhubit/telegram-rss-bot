# Telegram RSS Bot
Simple RSS bot for Telegram.

## Requirements
- python 3 (tested on 3.8)
- feedparser==6.0.1
- python-dateutil==2.8.1
- urllib3==1.25.10
- requests==2.24.0

## How to use
Install requirements:
```
pip install -r requirements.txt
```
create config file:
```
cp config.example.py config.py
```
and edit to fits your data Then start:
```
python3 main.py
```
## Credits
This bot is based on [jimocic](https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd) work.