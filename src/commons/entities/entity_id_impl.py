import uuid

from commons.entities.base import EntityId, EntityIdFactory


class UUIDEntityIdFactory(EntityIdFactory):
    """
    Фабрика для создания UUID идентификаторов сущностей.
    Реализует протокол EntityIdFactory.
    """

    def __call__(self) -> EntityId:
        """
        Создаёт новый UUID идентификатор сущности
        """
        return uuid.uuid4()
