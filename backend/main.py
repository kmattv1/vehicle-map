from fastapi import FastAPI, Depends
from functools import lru_cache
from starlette_prometheus import metrics, PrometheusMiddleware

from src.controllers.get_availability import GetAvailability
from src.controllers.get_availability_interface import GroupType
from src.use_cases.vehicle_info_mapper import VehicleInfoMapper
from src.use_cases.vehicle_info_mapper_interface import VehicleInfoMapperInterface
# from tests.mock_data.mocked_vehicle_info import MockVehicleInfo
from src.repositories.vehicle_info_interface import VehicleInfoInterface
from src.repositories.vehicle_info import VehicleInfo
from src.config.settings import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get('/vehicles')
async def get_vehicles(settings: Settings = Depends(get_settings), group: GroupType = GroupType.ALL):
    # vehicle_info: VehicleInfoInterface = MockVehicleInfo()
    vehicle_info: VehicleInfoInterface = VehicleInfo(settings)
    vehicle_info_mapper: VehicleInfoMapperInterface = VehicleInfoMapper()
    get_availability = GetAvailability(vehicle_info, vehicle_info_mapper)

    return await get_availability.get_device_by_group(group)


app.add_middleware(PrometheusMiddleware)
app.add_route('/metrics', metrics)
