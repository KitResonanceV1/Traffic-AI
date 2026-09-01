"""Headless runner script"""
from __future__ import annotations

from traffic_ai.simulation.world import World
from traffic_ai.simulation.intersection import Intersection
from traffic_ai.simulation.traffic_light import TrafficLight


def build_world(seed: int = 42):
    w = World(dt=1.0, seed=seed)
    # single intersection at center
    it = Intersection(id='I0', position=(50,25), traffic_light=TrafficLight())
    w.intersections = [it]
    w.attach_controller()
    return w


def run_headless(steps: int = 100, seed: int = 42):
    w = build_world(seed)
    w.demand.spawn_rate = 0.3
    w.run(steps)
    return w

if __name__ == '__main__':
    w = run_headless(200)
    print('Completed:', w.metrics.get('completed',0))
