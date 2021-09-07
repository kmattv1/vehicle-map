from fastapi import FastAPI, Depends
from functools import lru_cache

from src.config.settings import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get('/')
async def root(settings: Settings = Depends(get_settings)):
    return settings.app_name
