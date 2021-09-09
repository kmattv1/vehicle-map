from dataclasses import dataclass
from enum import Enum
from typing import List


class VehicleType(Enum):
    ESCOOTER = "escooter"


@dataclass(order=True, frozen=True)
class RentalUris:
    android: str
    ios: str


@dataclass(order=True, frozen=True)
class Bike:
    bike_id: str
    lat: float
    lon: float
    is_reserved: bool
    is_disabled: bool
    vehicle_type_id: VehicleType
    current_range_meters: int
    pricing_plan_id: str
    rental_uris: RentalUris


@dataclass(order=True, frozen=True)
class Bikes:
    bikes: List[Bike]


@dataclass(order=True, frozen=True)
class FreeBikeResponse:
    data: Bikes
