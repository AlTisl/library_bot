from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    redis_host: SecretStr
    redis_port: SecretStr
    redis_username: SecretStr
    redis_password: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings() # type: ignore