from dataclasses import dataclass


@dataclass(frozen=True)
class BaseApplicationEvent:
    """Базовый класс для всех событий слоя приложения"""

    pass
