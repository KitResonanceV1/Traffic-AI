"""Simple traffic light implementation with phases"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional


class Phase:
    NS_GREEN = "NS_GREEN"
    NS_YELLOW = "NS_YELLOW"
    ALL_RED = "ALL_RED"
    EW_GREEN = "EW_GREEN"
    EW_YELLOW = "EW_YELLOW"

    ORDER = [NS_GREEN, NS_YELLOW, ALL_RED, EW_GREEN, EW_YELLOW, ALL_RED]


@dataclass
class TrafficLight:
    phase: str = Phase.NS_GREEN
    timer: float = 0.0
    durations: Dict[str, float] = field(default_factory=lambda: {
        Phase.NS_GREEN: 30.0,
        Phase.NS_YELLOW: 5.0,
        Phase.ALL_RED: 2.0,
        Phase.EW_GREEN: 30.0,
        Phase.EW_YELLOW: 5.0,
    })
    controller: Optional[object] = None

    def set_controller(self, controller: object):
        self.controller = controller

    def step(self, dt: float):
        if self.controller:
            action = self.controller.action_for(self)
            if action == 'CHANGE':
                self._change_phase()
            elif action == 'EXTEND' and self.phase in (Phase.NS_GREEN, Phase.EW_GREEN):
                self.durations[self.phase] = min(self.durations[self.phase] + 5.0, 60.0)
        self.timer += dt
        if self.timer >= self.durations.get(self.phase, 1.0):
            self._change_phase()

    def _change_phase(self):
        self.timer = 0.0
        order = Phase.ORDER
        idx = order.index(self.phase)
        idx = (idx + 1) % len(order)
        self.phase = order[idx]

    def can_go(self, direction: str) -> bool:
        if self.phase == Phase.NS_GREEN and direction == 'NS':
            return True
        if self.phase == Phase.EW_GREEN and direction == 'EW':
            return True
        return False

    def current_state(self) -> str:
        return self.phase
