from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_DIR = ".env"

class Settings(BaseSettings):
    bot_token: SecretStr
    
    dadata_token: SecretStr
    dadata_secret: SecretStr
    
    google_account_path: str
    sheet_name: str
    
    model_config = SettingsConfigDict(env_file=ENV_DIR, env_file_encoding='utf-8')


config = Settings()