from pydantic import BaseSettings

class Settings(BaseSettings):
    decisio_env: str = "dev"
    db_url: str = "sqlite:///./decisio.db"
    api_url: str = "http://localhost:8000"

    class Config:
        env_file = ".env"

settings = Settings()