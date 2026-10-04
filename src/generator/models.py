from __future__ import annotations
import enum
from dataclasses import dataclass
from datetime import datetime


class WeatherType(enum.StrEnum):
    CLEAR = "clear"
    CLOUDY = "cloudy"
    FOG = "fog"
    RAINY = "rainy"
    SNOWY = "snowy"
    STORMY = "stormy"

@dataclass
class Station:
    stationID: int
    name: str
    city: str
    latitude: float
    longitude: float
    altitude: float


class WeatherReading:
    station_id: int
    timestamp: datetime
    temperature_celsus: float
    humidity_percent: float
    wind_speed_ms: float
    wind_direction_degrees: float
    weather_type: WeatherType
    is_anomaly: bool

Stations = list[Station]

print(f"\n\n{Station}")
print(f"1")
print(f"2")