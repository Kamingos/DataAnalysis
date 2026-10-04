from dataclasses import dataclass
from functools import lru_cache

from pydantic.v1 import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

print(1111)

class ClickHouseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CLICKHOUSE_",
        env_file=".env",
        extra="ignore",
        case_sensitive=False,)

    # TODO
    host: str = Field(default="localhost")
    port: int = Field(default=9000, ge=1, le=65535)
    database: str = Field(default="default")
    user: str = Field(default="default")
    password: str = Field(default="")
    database: str = Field(default="default")
    table: str = Field(default="weather_readings")

class GeneratorSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="GENERATOR_",
        env_file=".env",
        extra="ignore",
        case_sensitive=False,)

    batch_size: int = Field(default=1000, ge=1)
    interval_seconds: float = Field(default=1.0, ge=0.0)
    seed: int = Field(default=42, ge=0)
    anomaly_probability: float = Field(default=0.02, ge=0.0, le=1.0)
    anomaly_strange: float = Field(default=3.0, ge=0.0)
    cities: str = Field(default="London, Paris, New York, Tokyo")

    # Сервисные поля
    log_level: str = Field(default="INFO")
    retry_max_attempts: int = Field(default=5, ge=1)
    retry_base_delay: float = Field(default=0.5, ge=0.0)
    retry_max_delay: float = Field(default=30.0, ge=0.0)
    retry_backoff_factor: float = Field(default=2.0, ge=1.0)

    @property
    def city_list(self) -> list[str]:
        return [city.strip() for city in self.cities.split(",") if city.strip()]

@dataclass(frozen=True, slots=True)
class Settings:
    clickhouse: ClickHouseSettings
    generator: GeneratorSettings

@lru_cache
def get_settings() -> Settings:
    clickhouse_settings = ClickHouseSettings()
    generator_settings = GeneratorSettings()
    return Settings(clickhouse=clickhouse_settings, generator=generator_settings)