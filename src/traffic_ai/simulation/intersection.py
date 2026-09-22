"""Intersection model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from traffic_ai.simulation.traffic_light import TrafficLight


Point = Tuple[float, float]


@dataclass
class Intersection:
    """A road intersection controlled by one traffic light."""

    id: str
    position: Point
    traffic_light: TrafficLight | None = None

    def __post_init__(self) -> None:
        if self.traffic_light is None:
            self.traffic_light = TrafficLight()