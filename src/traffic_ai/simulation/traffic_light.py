"""Traffic light state machine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


class Phase:
    """Valid traffic-light phases."""

    NS_GREEN = "NS_GREEN"
    NS_YELLOW = "NS_YELLOW"
    ALL_RED_AFTER_NS = "ALL_RED_AFTER_NS"
    EW_GREEN = "EW_GREEN"
    EW_YELLOW = "EW_YELLOW"
    ALL_RED_AFTER_EW = "ALL_RED_AFTER_EW"

    ORDER = (
        NS_GREEN,
        NS_YELLOW,
        ALL_RED_AFTER_NS,
        EW_GREEN,
        EW_YELLOW,
        ALL_RED_AFTER_EW,
    )


@dataclass
class TrafficLight:
    """A two-direction traffic light."""

    phase: str = Phase.NS_GREEN
    timer: float = 0.0

    durations: Dict[str, float] = field(
        default_factory=lambda: {
            Phase.NS_GREEN: 30.0,
            Phase.NS_YELLOW: 5.0,
            Phase.ALL_RED_AFTER_NS: 2.0,
            Phase.EW_GREEN: 30.0,
            Phase.EW_YELLOW: 5.0,
            Phase.ALL_RED_AFTER_EW: 2.0,
        }
    )

    def __post_init__(self) -> None:
        if self.phase not in Phase.ORDER:
            raise ValueError(
                f"Invalid traffic-light phase: {self.phase}"
            )

        for phase, duration in self.durations.items():
            if duration <= 0:
                raise ValueError(
                    f"Duration for {phase} must be greater than 0"
                )

    def step(self, dt: float) -> None:
        """Advance the traffic light by dt seconds."""

        if dt <= 0:
            raise ValueError("dt must be greater than 0")

        self.timer += dt

        while self.timer >= self.durations[self.phase]:
            self.timer -= self.durations[self.phase]
            self._change_phase()

    def _change_phase(self) -> None:
        """Move to the next safe phase."""

        index = Phase.ORDER.index(self.phase)
        self.phase = Phase.ORDER[
            (index + 1) % len(Phase.ORDER)
        ]

    def can_go(self, direction: str) -> bool:
        """Return whether traffic in a direction has a green light."""

        if direction == "NS":
            return self.phase == Phase.NS_GREEN

        if direction == "EW":
            return self.phase == Phase.EW_GREEN

        raise ValueError(f"Unknown direction: {direction}")

    def current_state(self) -> str:
        """Return the current phase."""

        return self.phase