from pydantic import BaseSettings


class Settings(BaseSettings):
    iq_air_api_key: str
    iq_air_api_url: str
    open_meteo_api_url: str
    ninjas_api_url: str
    ninjas_api_key: str

    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_database: str

    class Config:
        env_file = "ENV/local.env"
        env_file_encoding = "utf-8"


settings = Settings()
