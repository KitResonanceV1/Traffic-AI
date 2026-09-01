"""
Minimal World: discrete-time simulation engine for Phase 1.
"""
from __future__ import annotations

from typing import List


class World:
    def __init__(self, dt: float = 1.0):
        self.dt = dt
        self.time = 0.0
        self.steps_taken = 0

    def step(self):
        """Advance the simulation by one time step."""
        self.time += self.dt
        self.steps_taken += 1

    def run(self, steps: int):
        for _ in range(steps):
            self.step()
