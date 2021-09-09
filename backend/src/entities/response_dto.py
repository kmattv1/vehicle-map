from dataclasses import dataclass
from enum import Enum
from typing import List


class VehicleType(Enum):
    ESCOOTER = "escooter"


@dataclass(order=True, frozen=True)
class Vehicle:
    id: str
    lat: float
    lon: float
    vehicle_type_id: VehicleType
    pricing_description: str


@dataclass(order=True, frozen=True)
class VehiclesCategorizedByAvailability:
    available: List[Vehicle]
    reserved: List[Vehicle]
    disabled: List[Vehicle]


@dataclass(order=True, frozen=True)
class Response:
    categorized_vehicles: VehiclesCategorizedByAvailability

