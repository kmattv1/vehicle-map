from fastapi import FastAPI, Depends
from functools import lru_cache

from src.repositories.vehicle_info_interface import VehicleInfoInterface
from src.repositories.vehicle_info import VehicleInfo
from src.config.settings import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get('/')
async def root(settings: Settings = Depends(get_settings)):
    vehicleInfo: VehicleInfoInterface = VehicleInfo(settings)
    return await vehicleInfo.get_availability_data()
