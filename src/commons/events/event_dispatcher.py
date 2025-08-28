from abc import abstractmethod
from collections.abc import Callable
from typing import Protocol, runtime_checkable

from commons.events import BaseApplicationEvent, BaseDomainEvent

EventAlias = BaseDomainEvent | BaseApplicationEvent
HandlerAlias = Callable[[EventAlias], None]


@runtime_checkable
class EventDispatcher(Protocol):
    """
    Обработчик событий приложения.

    Обрабатывает события доменного слоя и слоя приложения.
    """

    @abstractmethod
    def dispatch(
        self,
        event: BaseDomainEvent | BaseApplicationEvent,
    ) -> None: ...
