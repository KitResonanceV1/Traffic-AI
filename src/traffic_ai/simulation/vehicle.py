"""Vehicle dynamics simplified for Phase 1"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import math


@dataclass
class Vehicle:
    id: int
    position: Tuple[float, float]
    route: List[Tuple[float, float]]
    max_speed: float = 10.0
    accel: float = 2.0
    velocity: float = 0.0
    waiting: bool = False
    completed: bool = False
    waiting_time: float = 0.0
    total_travel_time: float = 0.0

    def step(self, dt: float, world: object):
        if self.completed:
            return
        self.total_travel_time += dt
        if not self.route:
            self.completed = True
            return
        target = self.route[0]
        dx = target[0] - self.position[0]
        dy = target[1] - self.position[1]
        dist = math.hypot(dx, dy)
        if dist < 0.5:
            self.position = target
            self.route.pop(0)
            return
        desired_speed = self.max_speed
        if self.velocity < desired_speed:
            self.velocity = min(desired_speed, self.velocity + self.accel * dt)
        move = min(self.velocity * dt, dist)
        ux = dx / dist
        uy = dy / dist
        self.position = (self.position[0] + ux * move, self.position[1] + uy * move)
        if self.velocity < 0.1:
            self.waiting = True
            self.waiting_time += dt
        else:
            self.waiting = False
