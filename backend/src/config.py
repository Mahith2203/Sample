from pydantic import BaseSettings

class Settings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    upload_dir: str = "./uploads"

    class Config:
        env_file = ".env"

settings = Settings()