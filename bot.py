import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

url = "https://www.mixvale.com.br/?s=gta+vi"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("a")

for article in articles:

    title = article.get_text()

    if "GTA" in title:

        link = article.get("href")

        title_he = GoogleTranslator(source='auto', target='iw').translate(title)

        message = {
            "username": "GTA VI News",
            "content": f"🎮 חדשות GTA VI\n\n{title_he}\n\n{link}"
        }

        requests.post(WEBHOOK, json=message)

        break
