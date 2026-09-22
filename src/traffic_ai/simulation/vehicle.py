"""Vehicle model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


Point = Tuple[float, float]


@dataclass
class Vehicle:
    """A vehicle moving through the simulation."""

    id: int
    position: Point

    max_speed: float = 10.0
    acceleration: float = 2.0

    velocity: float = 0.0
    waiting: bool = False
    waiting_time: float = 0.0
    total_travel_time: float = 0.0
    completed: bool = False

    def step(self, dt: float) -> None:
        """Advance the vehicle using simple acceleration."""

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        if self.completed:
            return

        self.total_travel_time += dt

        self.velocity = min(
            self.max_speed,
            self.velocity + self.acceleration * dt,
        )

        distance = self.velocity * dt

        self.position = (
            self.position[0],
            self.position[1] + distance,
        )

        self.waiting = self.velocity <= 0.0

        if self.waiting:
            self.waiting_time += dt