import asyncio
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

async def main():
    print("Бот запущен! Ссылка вставлена, окошко должно работать.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())