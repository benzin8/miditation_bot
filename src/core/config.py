from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    admin_id: int
    db_url: str
    # app_host: str
    # app_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


def load_config() -> Settings:
    return Settings()