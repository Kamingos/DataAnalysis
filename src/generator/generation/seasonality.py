from datetime import datetime
import math


def diurnal_factor(at: datetime) -> float:
    hour = at.hour + at.minute / 60.0
    return math.cos(2.0 * math.pi * (hour-15) / 24.0)

def annual_factor(at: datetime) -> float | int:
    day_of_the_year = float(at.timetuple().tm_yday)
    return math.cos(2.0 * math.pi * (day_of_the_year - 196) / 365.25)