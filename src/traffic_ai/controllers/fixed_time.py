"""Fixed-time traffic-light controller."""

from __future__ import annotations

from traffic_ai.controllers.base import Controller


class FixedTimeController(Controller):
    """Baseline controller using predetermined phase durations."""

    def __init__(
        self,
        ns_green: float = 30.0,
        ew_green: float = 30.0,
        yellow: float = 5.0,
        all_red: float = 2.0,
    ) -> None:
        for name, duration in {
            "ns_green": ns_green,
            "ew_green": ew_green,
            "yellow": yellow,
            "all_red": all_red,
        }.items():
            if duration <= 0:
                raise ValueError(f"{name} must be greater than 0")

        self.ns_green = ns_green
        self.ew_green = ew_green
        self.yellow = yellow
        self.all_red = all_red

    def action(self, state: object) -> str:
        """Return the default action.

        The fixed-time controller does not make dynamic decisions.
        Traffic-light timing is configured when the controller is created.
        """
        return "KEEP"
