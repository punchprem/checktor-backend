from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    debug: bool

settings = Settings(
    _env_file=".env",  
    _env_file_encoding="utf-8"
)
