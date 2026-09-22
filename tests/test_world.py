from traffic_ai.simulation.world import World


def test_world_starts_at_zero() -> None:
    world = World(dt=1.0)

    assert world.time == 0.0
    assert world.steps_taken == 0


def test_world_step() -> None:
    world = World(dt=0.5)

    world.step()

    assert world.time == 0.5
    assert world.steps_taken == 1


def test_world_run() -> None:
    world = World(dt=0.5)

    world.run(10)

    assert world.time == 5.0
    assert world.steps_taken == 10