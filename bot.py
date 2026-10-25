import asyncio
import os
import threading
from http.server import BaseHTTPRequestHandler
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultAudio

BOT_TOKEN = os.getenv("BOT_TOKEN")


AUDIO_FILES = {

    "Утонул" : "https://files.catbox.moe/8eu2x3.mp3",
    "Тимур" : "https://files.catbox.moe/nea7vv.mp3",
    "Сюда" : "https://files.catbox.moe/gkt7gu.mp3"

    }

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.inline_query()
async def inline_sounds(query: types.InlineQuery):
    results = []
    for i, (title, audio_url) in enumerate(AUDIO_FILES.items()):
        results.append(
            InlineQueryResultAudio(
                id=str(i),
                audio_url=audio_url, 
                title=title          
            )
        )
    await query.answer(results=results, cache_time=1)

    class Handler(BaseHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

async def main():
    threading.Thread(target=run_server, daemon=True).start()
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())