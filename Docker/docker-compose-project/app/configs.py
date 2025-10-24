from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MYSQL_ROOT_PASSWORD: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_HOST: str
    MYSQL_PORT: str

    class Config:
        env_file = ".env"


settings = Settings()

