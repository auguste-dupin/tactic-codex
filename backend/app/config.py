from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mode: str = "STUDIO"
    database_url: str = "sqlite:///./tactic.db"
    secret_key: str = "change_me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
