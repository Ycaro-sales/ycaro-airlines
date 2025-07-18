from dataclasses import field
from datetime import datetime
from uuid import UUID, uuid4
from typing import ClassVar, Dict, Any, Unpack, Self
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    instances: ClassVar[Dict[UUID, Self]]

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = datetime.now()

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        cls.instances = {}
        super().__init_subclass__(**kwargs)

    @classmethod
    def create(cls, /, **data: Any) -> Self | None:
        try:
            instance = cls(**data)
            cls.instances[instance.id] = instance
        except (ValidationError, TypeError) as e:
            print(f"Invalid model. Error: {e}")
            return None

        return instance

    @classmethod
    def delete(cls, id: UUID) -> None:
        if cls.instances.get(id) is None:
            return None
        del cls.instances[id]

    @classmethod
    def update(cls, id: UUID, **kwargs):
        try:
            if model := cls.instances.get(id):
                model.update(**kwargs)
                return model
            else:
                return None

        except (TypeError, ValidationError) as e:
            print(f"Invalid Model. Error: {e}")
            return None

    @classmethod
    def get(cls, id: UUID) -> Self | None:
        return cls.instances.get(id)

    # TODO: Criar filtros
    @classmethod
    def list(cls):
        return cls.instances.values()
