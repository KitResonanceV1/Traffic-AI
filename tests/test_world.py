def test_world_steps():
    from traffic_ai.simulation.world import World

    w = World(dt=0.5)
    assert w.time == 0.0
    w.step()
    assert w.time == 0.5
    w.run(4)
    assert w.steps_taken == 5
    assert w.time == 2.5
