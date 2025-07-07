from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """
    Application configuration settings.
    """
    app_name: str = Field(default="DLEEL", env="APP_NAME")
    version: str = Field(default="1.0.0", env="APP_VERSION")
    debug: bool = Field(default=False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"