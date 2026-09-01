"""Intersection wrapper that holds a traffic light"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
from traffic_ai.simulation.traffic_light import TrafficLight


@dataclass
class Intersection:
    id: str
    position: Tuple[float, float]
    traffic_light: TrafficLight = None

    def __post_init__(self):
        if self.traffic_light is None:
            self.traffic_light = TrafficLight()
