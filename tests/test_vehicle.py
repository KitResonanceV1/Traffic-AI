from traffic_ai.simulation.vehicle import Vehicle


def test_vehicle_accelerates_on_open_road() -> None:
    vehicle = Vehicle(
        id=1,
        position=(0.0, 0.0),
    )

    vehicle.step(dt=0.1)

    assert vehicle.acceleration > 0.0
    assert vehicle.velocity > 0.0
    assert vehicle.velocity <= vehicle.max_speed


def test_vehicle_slows_down_when_approaching_vehicle() -> None:
    vehicle = Vehicle(
        id=1,
        position=(0.0, 0.0),
        velocity=10.0,
    )

    acceleration = vehicle.desired_acceleration(
        gap=10.0,
        relative_speed=5.0,
    )

    assert acceleration < 0.0


def test_vehicle_brakes_when_gap_is_zero() -> None:
    vehicle = Vehicle(
        id=1,
        position=(0.0, 0.0),
        velocity=10.0,
    )

    acceleration = vehicle.desired_acceleration(
        gap=0.0,
    )

    assert acceleration == -vehicle.comfortable_deceleration


def test_vehicle_never_has_negative_speed() -> None:
    vehicle = Vehicle(
        id=1,
        position=(0.0, 0.0),
        velocity=1.0,
    )

    vehicle.step(
        dt=1.0,
        gap=0.1,
    )

    assert vehicle.velocity >= 0.0


def test_vehicle_does_not_exceed_max_speed() -> None:
    max_speed = 13.9

    vehicle = Vehicle(
        id=1,
        position=(0.0, 0.0),
        velocity=max_speed,
    )

    vehicle.step(dt=1.0)

    assert vehicle.velocity <= max_speed