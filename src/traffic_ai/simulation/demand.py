"""Traffic demand generation."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class Demand:
    """Generate vehicles according to a configurable arrival rate."""

    spawn_rate: float = 0.2
    seed: int = 42

    def __post_init__(self) -> None:
        if self.spawn_rate < 0:
            raise ValueError("spawn_rate must not be negative")

        self._random = random.Random(self.seed)
        self._next_vehicle_id = 1

    def should_spawn(self, dt: float) -> bool:
        """Return whether a vehicle should arrive during this time step."""

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        probability = min(1.0, self.spawn_rate * dt)
        return self._random.random() < probability

    def next_vehicle_id(self) -> int:
        """Return a unique vehicle ID."""
        vehicle_id = self._next_vehicle_id
        self._next_vehicle_id += 1
        return vehicle_id