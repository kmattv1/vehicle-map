import json

from src.entities.free_bike_dto import FreeBikeResponse
from src.entities.pricing_plans_dto import PricingPlansResponse
from src.repositories.vehicle_info_interface import VehicleInfoInterface, VehicleInfoData


class MockVehicleInfo(VehicleInfoInterface):
    def __init__(self):
        with open("./tests/mock_data/pricing.json", "r") as pricing_file:
            self.pricing_info = json.load(pricing_file)
        with open("./tests/mock_data/vehicle_info.json", "r") as vehicle_info_file:
            self.availability_info = json.load(vehicle_info_file)
        pass

    async def get_price_data(self):
        return self.pricing_info

    async def get_availability_data(self):
        return self.availability_info

    async def get_price_and_availability_data(self) -> VehicleInfoData:
        return VehicleInfoData(
            bikes=FreeBikeResponse(data=self.availability_info['data']),
            plans=PricingPlansResponse(data=self.pricing_info['data'])
        )
