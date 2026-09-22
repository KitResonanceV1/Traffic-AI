"""Core simulation world."""

from __future__ import annotations


class World:
    """Discrete-time simulation world."""

    def __init__(self, dt: float = 1.0) -> None:
        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        self.dt = dt
        self.time = 0.0
        self.steps_taken = 0

    def step(self) -> None:
        """Advance the simulation by one time step."""
        self.time += self.dt
        self.steps_taken += 1

    def run(self, steps: int) -> None:
        """Advance the simulation by a fixed number of steps."""
        if steps < 0:
            raise ValueError("steps must not be negative")

        for _ in range(steps):
            self.step()