from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.entities.free_bike_dto import FreeBikeResponse
from src.entities.pricing_plans_dto import PricingPlansResponse


@dataclass(order=True, frozen=True)
class VehicleInfoData:
    bikes: FreeBikeResponse
    plans: PricingPlansResponse


class VehicleInfoInterface(ABC):

    @abstractmethod
    def get_availability_data(self) -> FreeBikeResponse:
        """get vehicle availability information from downstream"""
        pass

    @abstractmethod
    def get_price_data(self) -> PricingPlansResponse:
        """get vehicle price information from downstream"""
        pass

    @abstractmethod
    def get_price_and_availability_data(self) -> VehicleInfoData:
        """get vehicle availability and price information from downstream"""
        pass
