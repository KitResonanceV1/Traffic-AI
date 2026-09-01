"""Road model for Phase 1: simple straight roads"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Road:
    id: str
    start: Tuple[float, float]
    end: Tuple[float, float]
    length: float = None

    def __post_init__(self):
        if self.length is None:
            dx = self.end[0] - self.start[0]
            dy = self.end[1] - self.start[1]
            self.length = (dx * dx + dy * dy) ** 0.5
