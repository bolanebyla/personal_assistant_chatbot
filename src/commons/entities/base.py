from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Protocol, runtime_checkable

from commons.datetime_utils import now_tz
from commons.events import BaseDomainEvent


@runtime_checkable
class EntityId(Protocol):
    """
    Протокол для идентификатора сущности.
    Поддерживает все необходимые методы для первичного ключа.
    """

    def __str__(self) -> str: ...

    def __hash__(self) -> int: ...

    def __eq__(self, other: Any) -> bool: ...

    def __lt__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool: ...

    def __gt__(self, other: Any) -> bool: ...

    def __ge__(self, other: Any) -> bool: ...


@runtime_checkable
class EntityIdFactory(Protocol):
    """
    Протокол для фабрики создания идентификаторов сущностей.
    При вызове возвращает EntityId.
    """

    def __call__(self) -> EntityId: ...


@dataclass
class BaseEntity:
    """
    Базовый класс сущности
    """

    id: EntityId
    created_at: datetime
    updated_at: datetime

    __domain_events: list[BaseDomainEvent] = field(default_factory=list)

    def _add_domain_event(self, event: BaseDomainEvent) -> None:
        """Добавляет доменное событие в список событий сущности"""
        self.__domain_events.append(event)

    @property
    def domain_events(self) -> list[BaseDomainEvent]:
        """Возвращает список всех доменных событий сущности"""
        return self.__domain_events.copy()

    def set_updated_at(self) -> None:
        """
        Устанавливает время обновления как текущее время
        """
        self.updated_at = now_tz()

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает сущности только по id
        """
        if not isinstance(other, BaseEntity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        """
        Хеширует сущность только по id
        """
        return hash(self.id)

    def __lt__(self, other: object) -> bool:
        """
        Сравнивает сущности по id для сортировки
        """
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id < other.id

    def __le__(self, other: object) -> bool:
        """
        Сравнивает сущности по id для сортировки
        """
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id <= other.id

    def __gt__(self, other: object) -> bool:
        """
        Сравнивает сущности по id для сортировки
        """
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id > other.id

    def __ge__(self, other: object) -> bool:
        """
        Сравнивает сущности по id для сортировки
        """
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return self.id >= other.id


@dataclass
class BaseAggregateRoot(BaseEntity):
    """
    Базовый класс для корня агрегата
    """

    pass
