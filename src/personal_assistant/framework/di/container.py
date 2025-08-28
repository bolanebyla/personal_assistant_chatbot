from dishka import AsyncContainer, make_async_container
from dishka.integrations.aiogram import setup_dishka

from personal_assistant.framework.di.providers import DBRepositoriesProvider, UseCasesProvider
from personal_assistant.infrastructure.tg_bot import tg_bot_dispatcher


def create_container() -> AsyncContainer:
    container = make_async_container(
        DBRepositoriesProvider(),
        UseCasesProvider(),
    )

    setup_dishka(container=container, router=tg_bot_dispatcher, auto_inject=True)
    return container
