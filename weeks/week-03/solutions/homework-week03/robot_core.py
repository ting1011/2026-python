"""Week 03 Robot Lost core logic (no pygame dependency)."""

from __future__ import annotations

from dataclasses import dataclass

DIRECTIONS = ["N", "E", "S", "W"]
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Robot:
    x: int
    y: int
    direction: str
    lost: bool = False


class World:
    def __init__(self, width: int, height: int) -> None:
        if width < 0 or height < 0:
            raise ValueError("width and height must be >= 0")
        self.width = width
        self.height = height
        self.scents: set[tuple[int, int, str]] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height


def turn_left(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction: str) -> str:
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def next_position(x: int, y: int, direction: str) -> tuple[int, int]:
    dx, dy = MOVE[direction]
    return x + dx, y + dy


def execute_command(world: World, robot: Robot, cmd: str) -> Robot:
    if robot.lost:
        return robot

    if cmd == "L":
        robot.direction = turn_left(robot.direction)
        return robot

    if cmd == "R":
        robot.direction = turn_right(robot.direction)
        return robot

    if cmd == "F":
        nx, ny = next_position(robot.x, robot.y, robot.direction)
        if world.in_bounds(nx, ny):
            robot.x, robot.y = nx, ny
            return robot

        scent_key = (robot.x, robot.y, robot.direction)
        if scent_key in world.scents:
            return robot

        world.scents.add(scent_key)
        robot.lost = True
        return robot

    raise ValueError(f"invalid command: {cmd}")


def execute_commands(world: World, robot: Robot, commands: str) -> Robot:
    for c in commands:
        execute_command(world, robot, c)
        if robot.lost:
            break
    return robot


def format_robot(robot: Robot) -> str:
    base = f"{robot.x} {robot.y} {robot.direction}"
    if robot.lost:
        return base + " LOST"
    return base
