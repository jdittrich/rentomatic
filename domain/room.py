import uuid
import dataclasses


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod #which is a sort of constructor
    def from_dict(cls, d):
            return cls(**d) #destructurizes the dict.
