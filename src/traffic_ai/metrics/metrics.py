"""Metrics collected from a traffic simulation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Metrics:
    """Basic simulation metrics."""

    completed_vehicles: int = 0
    total_waiting_time: float = 0.0
    total_travel_time: float = 0.0
    collisions: int = 0

    def record_waiting(self, seconds: float) -> None:
        if seconds < 0:
            raise ValueError("seconds must not be negative")

        self.total_waiting_time += seconds

    def record_travel(self, seconds: float) -> None:
        if seconds < 0:
            raise ValueError("seconds must not be negative")

        self.total_travel_time += seconds

    def record_completion(self, travel_time: float) -> None:
        if travel_time < 0:
            raise ValueError("travel_time must not be negative")

        self.completed_vehicles += 1
        self.total_travel_time += travel_time

    def record_collision(self) -> None:
        self.collisions += 1