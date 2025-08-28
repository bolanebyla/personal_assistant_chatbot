import asyncio
import logging
import sys

from personal_assistant.framework.di.container import create_container
from personal_assistant.infrastructure.tg_bot import (
    tg_bot,
    tg_bot_dispatcher,
)

container = create_container()


async def start_tg_bot_polling() -> None:
    await tg_bot_dispatcher.start_polling(tg_bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_tg_bot_polling())
