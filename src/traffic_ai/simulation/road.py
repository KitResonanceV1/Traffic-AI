"""Road definitions for the traffic simulation."""

from __future__ import annotations

from dataclasses import dataclass
from math import hypot
from typing import Tuple


Point = Tuple[float, float]


@dataclass
class Road:
    """A straight road segment connecting two points."""

    id: str
    start: Point
    end: Point

    @property
    def length(self) -> float:
        """Return the geometric length of the road."""
        return hypot(
            self.end[0] - self.start[0],
            self.end[1] - self.start[1],
        )