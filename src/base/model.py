from datetime import date
from uuid import UUID, uuid4
from typing import Dict, List, Tuple, NewType
import peewee

peewee.Model


class Model:
    _items: Dict[UUID, "Model"] = {}
    FIELDS: Dict[str, type] = {}

    def __init__(self) -> None:
        self.id: UUID = uuid4()
        self.created_at: date = date.today()
        for k, v in self.FIELDS.items():
            self.__setattr__(k, v)

    @classmethod
    def _create(cls, **kwargs) -> "Model":
        temp = cls()
        for i in cls.FIELDS.keys():
            pass
        cls._items[temp.id] = temp
        return temp

    @classmethod
    def create(cls) -> "Model":
        return cls._create()

    @classmethod
    def delete(cls, id: UUID) -> None:
        if cls._items.get(id) is None:
            return None
        del cls._items[id]

    # TODO: Atualmente essa funcao atualiza a instancia inteira mesmo
    # se tiver um atributo nao encontrado
    def update(self, **kwargs):
        for i, v in kwargs.items():
            if hasattr(self, i):
                self.__dict__[i] = v
            else:
                print(f"<{self.__class__.__name__}> doesnt have attribute {i}")
        print(f"updated {self.__class__.__name__}")

    @classmethod
    def get(cls, id: UUID):
        return cls._items.get(id)

    # TODO: Criar filtros
    @classmethod
    def list(cls, pagination: int = 50):
        models = []
        count = 1
        for i in cls._items.items():
            if count > pagination:
                break
            models.append(i)
            count += 1

        return cls._items.items()
