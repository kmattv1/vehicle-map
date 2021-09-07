from dataclasses import dataclass
from typing import List


@dataclass(order=True, frozen=True)
class Data:
    pass


@dataclass
class Response:
    data: List[Data]
