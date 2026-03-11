import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

url = "https://www.rockstargames.com/newswire"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

posts = soup.find_all("a")

for post in posts:
    text = post.get_text()
    
    if "GTA VI" in text or "Grand Theft Auto VI" in text:
        
        link = post.get("href")
        
        title_he = GoogleTranslator(source='auto', target='iw').translate(text)

        message = {
            "content": f"🎮 עדכון חדש על GTA VI\n\n{title_he}\n\nhttps://www.rockstargames.com{link}"
        }

        requests.post(WEBHOOK, json=message)
        break
