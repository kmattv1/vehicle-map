import json
from httpx import AsyncClient
import asyncio

from src.config.settings import Settings
from src.entities.pricing_plans_dto import PricingPlansResponse
from src.repositories.vehicle_info_interface import VehicleInfoInterface, VehicleInfoData
from src.entities.free_bike_dto import FreeBikeResponse


class VehicleInfo(VehicleInfoInterface):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.URL = self.settings.downstream_url
        MAX_IN_PARALLEL = 1000
        self.limit_sem = asyncio.Semaphore(MAX_IN_PARALLEL)

    async def pricing_request(self, client) -> PricingPlansResponse:
        async with self.limit_sem:
            response = await client.get(self.URL + "/system-pricing-plans",
                                        headers={"x-api-key": self.settings.api_key})
            resp = PricingPlansResponse(data=json.loads(response.text)['data'])
            return resp

    async def get_price_data(self) -> PricingPlansResponse:
        async with AsyncClient() as client:
            response = await asyncio.gather(self.pricing_request(client))
            return response[0]

    async def availability_request(self, client) -> FreeBikeResponse:
        async with self.limit_sem:
            response = await client.get(self.URL + "/free-bike-status",
                                        headers={"x-api-key": self.settings.api_key})
            resp = FreeBikeResponse(data=json.loads(response.text)['data'])
            return resp

    async def get_availability_data(self) -> FreeBikeResponse:
        async with AsyncClient() as client:
            response = await asyncio.gather(self.availability_request(client))
            return response[0]

    async def get_price_and_availability_data(self) -> VehicleInfoData:
        async with AsyncClient() as client:
            response = await asyncio.gather(self.availability_request(client), self.pricing_request(client))
            return VehicleInfoData(bikes=response[0], plans=response[1])
