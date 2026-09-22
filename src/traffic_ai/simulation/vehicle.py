"""Vehicle model with IDM car-following behavior."""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Tuple


Point = Tuple[float, float]


@dataclass
class Vehicle:
    """A vehicle using the Intelligent Driver Model (IDM)."""

    id: int
    position: Point

    max_speed: float = 13.9
    max_acceleration: float = 2.6
    comfortable_deceleration: float = 4.5

    min_gap: float = 2.5
    desired_headway: float = 1.2
    length: float = 5.0

    velocity: float = 0.0
    acceleration: float = 0.0

    waiting: bool = False
    waiting_time: float = 0.0
    total_travel_time: float = 0.0
    completed: bool = False

    def desired_acceleration(
        self,
        gap: float,
        relative_speed: float = 0.0,
    ) -> float:
        """Calculate acceleration using the Intelligent Driver Model."""

        if gap <= 0:
            return -self.comfortable_deceleration

        velocity = max(0.0, self.velocity)

        desired_gap = (
            self.min_gap
            + velocity * self.desired_headway
            + (
                velocity * relative_speed
                / (
                    2.0
                    * sqrt(
                        self.max_acceleration
                        * self.comfortable_deceleration
                    )
                )
            )
        )

        acceleration = self.max_acceleration * (
            1.0
            - (velocity / self.max_speed) ** 4
            - (desired_gap / gap) ** 2
        )

        return acceleration

    def step(
        self,
        dt: float,
        gap: float | None = None,
        relative_speed: float = 0.0,
    ) -> None:
        """Advance the vehicle by one simulation step."""

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        if self.completed:
            return

        self.total_travel_time += dt

        if gap is None:
            acceleration = self.max_acceleration * (
                1.0 - (self.velocity / self.max_speed) ** 4
            )
        else:
            acceleration = self.desired_acceleration(
                gap=gap,
                relative_speed=relative_speed,
            )

        self.acceleration = acceleration

        self.velocity = max(
            0.0,
            min(
                self.max_speed,
                self.velocity + acceleration * dt,
            ),
        )

        distance = self.velocity * dt

        self.position = (
            self.position[0],
            self.position[1] + distance,
        )

        self.waiting = self.velocity <= 0.01

        if self.waiting:
            self.waiting_time += dt