from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from returns.result import Result

from src.entities.free_bike_dto import Bike
from src.entities.pricing_plans_dto import Plan
from src.entities.response_dto import VehiclesCategorizedByAvailability


@dataclass(order=True, frozen=True)
class BikeWithPrice(Bike):
    pricing_description: str


@dataclass(order=True, frozen=True)
class FilteredBikesWithPrice:
    available: List[BikeWithPrice]
    reserved: List[BikeWithPrice]
    disabled: List[BikeWithPrice]


class VehicleInfoMapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def group_and_map_data(vehicle_data: List[Bike],
                           pricing_data: List[Plan]) -> Result[VehiclesCategorizedByAvailability, Exception]:
        pass
