from __future__ import annotations

import enum
import random

class AnomalyKind(enum.StrEnum):
    HEAT_WAVE = 'heat_wave'
    COLD_SNAP = 'cold_snap'
    PRESSURE_DROP = 'pressure_drop'
    WIND_GUST = 'wind_gust'


class AnomalyPolicy:
    def __init__(self, probability: float | int, strength: float | int, rng: random.Random):
        ...

    @property
    def strength(self) -> float | int:
        return self._strength

    def decide(self) -> AnomalyKind | None:
        if self._rng.random() >= self._probability:
            return None
        return self._rng.choice(list[AnomalyKind](AnomalyKind))