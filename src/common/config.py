from pydantic_settings import BaseSettings, SettingsConfigDict

class WindsorSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="WINDSOR_", env_file=".env", extra="ignore")
    api_key: str = "sandbox-placeholder"
    base_url: str = "https://connectors.windsor.ai"
