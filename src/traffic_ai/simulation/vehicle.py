from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional
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
    # optional override for desired speed (used by higher-level controller)
    desired_speed_override: Optional[float] = None

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
        # determine desired speed (allow override from controller/simulator)
        desired_speed = self.desired_speed_override if self.desired_speed_override is not None else self.max_speed
        # accelerate or decelerate towards desired_speed
        if self.velocity < desired_speed:
            self.velocity = min(desired_speed, self.velocity + self.accel * dt)
        elif self.velocity > desired_speed:
            # simple deceleration using same accel as braking (could be a separate braking parameter)
            self.velocity = max(desired_speed, self.velocity - self.accel * dt)
        # move according to current velocity
        move = min(self.velocity * dt, dist)
        if dist != 0:
            ux = dx / dist
            uy = dy / dist
        else:
            ux = uy = 0.0
        self.position = (self.position[0] + ux * move, self.position[1] + uy * move)
        # update waiting state
        if self.velocity < 0.1:
            self.waiting = True
            self.waiting_time += dt
        else:
            self.waiting = False
