"""Tests added for new modules"""
from traffic_ai.simulation.traffic_light import TrafficLight, Phase
from traffic_ai.simulation.demand import Demand
from traffic_ai.simulation.vehicle import Vehicle
from traffic_ai.simulation.world import World
from traffic_ai.controllers.fixed_time import FixedTimeController


def test_traffic_light_cycles():
    tl = TrafficLight()
    seen = set()
    for _ in range(100):
        tl.step(1.0)
        seen.add(tl.phase)
    assert 'NS_GREEN' in seen
    assert 'EW_GREEN' in seen


def test_demand_spawns():
    d = Demand(spawn_rate=1.0, seed=1)
    w = World(dt=1.0)
    vehicles = d.spawn(w, 1.0)
    assert isinstance(vehicles, list)


def test_fixed_controller_sets():
    ctrl = FixedTimeController(ns_green=10, ew_green=8)
    tl = TrafficLight()
    assert ctrl.action_for(tl) == 'KEEP'
    assert tl.durations['NS_GREEN'] == 10
