import openai
import requests
import time

# === Налаштування ===
openai.api_key = "ТВОЯ_OPENAI_API_KEY"
bot_token = "ТВОЙ_TELEGRAM_BOT_TOKEN"
channel_username = "@Назва_твого_каналу"

# === Функція генерації тексту GPT ===
def generate_post(topic="Ідеї для постів у Telegram"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ти український Telegram-копірайтер, пиши короткі, цікаві пости для каналу."},
            {"role": "user", "content": f"Напиши пост на тему: {topic}"}
        ]
    )
    return response.choices[0].message.content.strip()

# === Публікація в Telegram ===
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": channel_username,
        "text": text,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=data)
    return r.json()

# === Основна логіка ===
if __name__ == "__main__":
    while True:
        topic = "Мотивація для підприємців"  # Можеш замінити або автоматизувати
        post = generate_post(topic)
        print("Згенеровано:", post)
        send_to_telegram(post)
        time.sleep(3600 * 6)  # Кожні 6 годин
