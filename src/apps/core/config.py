from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APPLICATION_NAME: str = "Oneiro Backend"
    ENVIRONMENT: str = "development"
    POSTGRES_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440 # 24 Hours
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080 # 7 Days
    
    # External Integration Keys
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    RESEND_API_KEY: str = ""
    EMAIL_FROM: str = "noreply@oneiro.com"
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        print(f"Environment initialized from: {Path(__file__).resolve().parent.parent.parent.parent}")
        env_file = Path(__file__).resolve().parent.parent.parent.parent / ".env"
        extra = "ignore"


settings = Settings()