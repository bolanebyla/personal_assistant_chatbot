import asyncio
import logging
import sys

from personal_assistant.infrastructure.tg_chat_bot import (
    tg_bot,
    tg_bot_dispatcher,
)


async def start_tg_bot_polling():
    await tg_bot_dispatcher.start_polling(tg_bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_tg_bot_polling())
