from traffic_ai.simulation.traffic_light import Phase, TrafficLight


def test_traffic_light_starts_with_ns_green() -> None:
    light = TrafficLight()

    assert light.current_state() == Phase.NS_GREEN
    assert light.can_go("NS")
    assert not light.can_go("EW")


def test_traffic_light_changes_to_ns_yellow() -> None:
    light = TrafficLight()

    light.step(30.0)

    assert light.current_state() == Phase.NS_YELLOW
    assert not light.can_go("NS")
    assert not light.can_go("EW")


def test_traffic_light_changes_to_ew_green() -> None:
    light = TrafficLight()

    light.step(30.0)
    light.step(5.0)
    light.step(2.0)

    assert light.current_state() == Phase.EW_GREEN
    assert not light.can_go("NS")
    assert light.can_go("EW")


def test_traffic_light_completes_full_cycle() -> None:
    light = TrafficLight()

    light.step(30.0)
    light.step(5.0)
    light.step(2.0)
    light.step(30.0)
    light.step(5.0)
    light.step(2.0)

    assert light.current_state() == Phase.NS_GREEN


def test_traffic_light_rejects_invalid_dt() -> None:
    light = TrafficLight()

    try:
        light.step(0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for dt <= 0")


def test_traffic_light_rejects_unknown_direction() -> None:
    light = TrafficLight()

    try:
        light.can_go("INVALID")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for unknown direction")