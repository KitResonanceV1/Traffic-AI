"""Adaptive traffic-light controller."""

from __future__ import annotations

from traffic_ai.controllers.base import Controller


class AdaptiveController(Controller):
    """Simple adaptive controller based on traffic demand."""

    def __init__(
        self,
        min_green: float = 10.0,
        max_green: float = 60.0,
    ) -> None:
        if min_green <= 0:
            raise ValueError("min_green must be greater than 0")

        if max_green < min_green:
            raise ValueError("max_green must be >= min_green")

        self.min_green = min_green
        self.max_green = max_green

    def action(self, state: object) -> str:
        """Return a control action from the current state.

        The full traffic-state model will be added later.
        """
        return "KEEP"