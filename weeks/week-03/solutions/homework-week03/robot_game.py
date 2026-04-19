"""Week 03 Robot Lost pygame demo.

Key controls:
- L/R/F: send one command
- N: new robot
- C: clear scents
- ESC: quit
"""

from __future__ import annotations

import sys

from robot_core import Robot, World, execute_command


def run_game() -> None:
    try:
        import pygame
    except Exception:
        print("pygame 尚未安裝，請先執行: python -m pip install pygame")
        return

    pygame.init()
    cell = 64
    margin = 24
    grid_w, grid_h = 5, 3
    panel_h = 160
    width = margin * 2 + (grid_w + 1) * cell
    height = margin * 2 + (grid_h + 1) * cell + panel_h

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Week03 Robot Lost")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 24)

    world = World(grid_w, grid_h)
    robot = Robot(0, 0, "N")
    history: list[str] = []

    def reset_robot() -> None:
        nonlocal robot
        robot = Robot(0, 0, "N")

    def draw() -> None:
        screen.fill((20, 26, 36))

        gx0, gy0 = margin, margin
        gx1 = gx0 + (grid_w + 1) * cell
        gy1 = gy0 + (grid_h + 1) * cell

        for x in range(grid_w + 2):
            px = gx0 + x * cell
            pygame.draw.line(screen, (80, 100, 120), (px, gy0), (px, gy1), 1)
        for y in range(grid_h + 2):
            py = gy0 + y * cell
            pygame.draw.line(screen, (80, 100, 120), (gx0, py), (gx1, py), 1)

        # scent markers
        for sx, sy, _ in world.scents:
            cx = gx0 + sx * cell + cell // 2
            cy = gy1 - sy * cell - cell // 2
            pygame.draw.circle(screen, (255, 200, 80), (cx, cy), 6)

        # robot triangle
        rx = gx0 + robot.x * cell + cell // 2
        ry = gy1 - robot.y * cell - cell // 2
        size = 18
        if robot.direction == "N":
            pts = [(rx, ry - size), (rx - size, ry + size), (rx + size, ry + size)]
        elif robot.direction == "E":
            pts = [(rx + size, ry), (rx - size, ry - size), (rx - size, ry + size)]
        elif robot.direction == "S":
            pts = [(rx, ry + size), (rx - size, ry - size), (rx + size, ry - size)]
        else:
            pts = [(rx - size, ry), (rx + size, ry - size), (rx + size, ry + size)]

        color = (255, 100, 100) if robot.lost else (80, 220, 170)
        pygame.draw.polygon(screen, color, pts)

        status_y = gy1 + 20
        lines = [
            f"Robot: ({robot.x}, {robot.y}) {robot.direction} {'LOST' if robot.lost else 'ALIVE'}",
            f"Scents: {sorted(world.scents)}",
            f"History: {''.join(history)}",
            "Keys: L/R/F move, N new robot, C clear scent, ESC quit",
        ]
        for i, line in enumerate(lines):
            surface = font.render(line, True, (230, 235, 240))
            screen.blit(surface, (margin, status_y + i * 30))

        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_n:
                    reset_robot()
                    history.clear()
                elif event.key == pygame.K_c:
                    world.scents.clear()
                elif event.key == pygame.K_l:
                    execute_command(world, robot, "L")
                    history.append("L")
                elif event.key == pygame.K_r:
                    execute_command(world, robot, "R")
                    history.append("R")
                elif event.key == pygame.K_f:
                    execute_command(world, robot, "F")
                    history.append("F")

        draw()
        clock.tick(30)


if __name__ == "__main__":
    run_game()
