from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", "dev.env"), env_file_encoding="utf-8", extra="ignore")

    OTEL_SERVICE_NAME: str = "password-generator-api"
    OTEL_PYTHON_LOG_LEVEL: str = "INFO"
    OTEL_SERVICE_NAMESPACE: str = "default"
    ENVIRONMENT: str = "development"
    SERVICE_OWNER_NAME: str = ""
    SERVICE_OWNER_URL: str = ""
    SERVICE_OWNER_CONTACT: str = ""
    SERVICE_OWNER_DISCORD: str = ""
    SERVICE_VERSION: str = ""
    COMMIT_HASH: str = ""
    COMMIT_BRANCH: str = ""
    DEPLOYMENT_USER: str = ""
    DEPLOYMENT_TRIGGER: str = ""
    
    # Pyroscope Configuration
    PYROSCOPE_SERVER_ADDRESS: str = "http://localhost:4040"
    PYROSCOPE_BASIC_AUTH_USERNAME: str = ""
    PYROSCOPE_BASIC_AUTH_PASSWORD: str = ""


settings = Settings()
