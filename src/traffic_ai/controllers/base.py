"""Base interface for traffic-light controllers."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Controller(ABC):
    """Base class for traffic-light control policies."""

    @abstractmethod
    def action(self, state: object) -> str:
        """Return the action requested from the controller."""
        raise NotImplementedError