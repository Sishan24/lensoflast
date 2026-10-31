from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ExpiryLens"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    max_upload_mb: int = 12
    cors_origins: str = "http://localhost:5173"
    mongodb_uri: str = ""
    mongodb_database: str = "expirylens"
    model_dir: str = "ml/artifacts"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def allowed_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
