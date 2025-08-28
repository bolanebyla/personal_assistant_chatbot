from dataclasses import dataclass


@dataclass(frozen=True)
class BaseDomainEvent:
    """Базовый класс для всех событий доменного слоя"""

    pass
