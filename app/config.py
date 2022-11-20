from pydantic import BaseSettings


class Settings(BaseSettings):
    iq_air_api_key: str
    iq_air_api_url: str
    open_meteo_api_url: str

    class Config:
        env_file = "ENV/local.env"
        env_file_encoding = "utf-8"


settings = Settings()
