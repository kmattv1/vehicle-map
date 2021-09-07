from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Vehicle BFF"
    downstream_url: str
    api_key: str

    class Config:
        env_file = ".env"
