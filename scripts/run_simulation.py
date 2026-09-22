"""Run a minimal Traffic-AI simulation."""

from traffic_ai.simulation.world import World


def main() -> None:
    world = World(dt=1.0)

    print("Traffic-AI simulation")
    print("---------------------")

    for _ in range(10):
        world.step()
        print(
            f"time={world.time:.1f}s "
            f"steps={world.steps_taken}"
        )


if __name__ == "__main__":
    main()