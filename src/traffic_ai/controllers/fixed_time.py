"""Fixed-time controller for traffic lights"""
from __future__ import annotations

class FixedTimeController:
    def __init__(self, ns_green: float = 30.0, ns_yellow: float = 5.0, all_red: float = 2.0, ew_green: float = 30.0, ew_yellow: float = 5.0):
        self.durations = {
            'NS_GREEN': ns_green,
            'NS_YELLOW': ns_yellow,
            'ALL_RED': all_red,
            'EW_GREEN': ew_green,
            'EW_YELLOW': ew_yellow,
        }

    def action_for(self, traffic_light: object) -> str:
        for k, v in self.durations.items():
            traffic_light.durations[k] = v
        return 'KEEP'
