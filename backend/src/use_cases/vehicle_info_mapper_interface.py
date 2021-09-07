from abc import ABC, abstractmethod
from typing import List
from returns.result import Result


class VehicleInfoMapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def filter_and_map_data(data: List[str]) -> Result[List[str], Exception]:
        pass
