"""Simple Poisson-like demand generator"""
from __future__ import annotations

from typing import List, Tuple
import random
import itertools
from traffic_ai.simulation.vehicle import Vehicle


class Demand:
    def __init__(self, spawn_rate: float = 0.2, seed: int = 42):
        self.spawn_rate = spawn_rate
        self.random = random.Random(seed)
        self._id_iter = itertools.count(1)

    def spawn(self, world, dt: float) -> List[Vehicle]:
        expected = self.spawn_rate * dt
        vehicles = []
        if self.random.random() < expected:
            entry_points = [ (0, 25), (50, 0), (100, 25), (50, 50) ]
            routes = [ [(100,25)], [(50,50)], [(0,25)], [(50,0)] ]
            idx = self.random.randrange(len(entry_points))
            pos = entry_points[idx]
            route = routes[idx][:]
            vid = next(self._id_iter)
            v = Vehicle(id=vid, position=pos, route=route)
            vehicles.append(v)
        return vehicles
