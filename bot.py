import os
import requests

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

message = {
    "content": "✅ בדיקת דמו: הבוט מחובר בהצלחה ושולח הודעות לדיסקורד"
}

requests.post(WEBHOOK, json=message)
print("Test message sent")
