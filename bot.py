import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

url = "https://www.mixvale.com.br/?s=gta+vi"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

article = soup.find("h2")

title = article.text
link = article.find("a")["href"]

title_he = GoogleTranslator(source='auto', target='iw').translate(title)

message = {
    "content": f"🎮 חדשות GTA VI\n\n{title_he}\n\n{link}"
}

requests.post(WEBHOOK, json=message)
