from abc import ABC, abstractmethod
from typing import List
from returns.result import Result

from backend.src.entities.downstream_dto import Data


class VehicleInfoMapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def filter_and_map_data(data: List[Data]) -> Result[List[Data], Exception]:
        pass
