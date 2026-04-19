from math import cos, sin, pi, atan2
from PIL import Image, ImageDraw, ImageFont

OUT_PATH = "replay.gif"
W, H = 640, 850

# Visual style close to the existing replay
BG = (10, 18, 30)
GRID_BG = (12, 20, 32)
GRID_LINE = (70, 84, 106)
PANEL_BG = (32, 43, 59)
TEXT = (230, 236, 243)
ROBOT = (72, 224, 181)

MARGIN = 30
GRID_SIZE = 560
CELL = GRID_SIZE / 10
GRID_X0 = MARGIN
GRID_Y0 = MARGIN
GRID_X1 = GRID_X0 + GRID_SIZE
GRID_Y1 = GRID_Y0 + GRID_SIZE

PANEL_X0 = 32
PANEL_Y0 = 610
PANEL_X1 = W - 32
PANEL_Y1 = H - 40

FRAMES = 72
RADIUS_CELL = 3.8
CENTER_CELL_X = 4.5
CENTER_CELL_Y = 4.5


def to_px(cell_x: float, cell_y: float) -> tuple[float, float]:
    x = GRID_X0 + (cell_x + 0.5) * CELL
    y = GRID_Y0 + (cell_y + 0.5) * CELL
    return x, y


def direction_label(dx: float, dy: float) -> str:
    # Up is negative y in image coordinates.
    dirs = [
        ("E", 0.0),
        ("SE", pi / 4),
        ("S", pi / 2),
        ("SW", 3 * pi / 4),
        ("W", pi),
        ("NW", -3 * pi / 4),
        ("N", -pi / 2),
        ("NE", -pi / 4),
    ]
    ang = atan2(dy, dx)
    best = min(dirs, key=lambda it: abs((ang - it[1] + pi) % (2 * pi) - pi))
    return best[0]


def triangle_points(cx: float, cy: float, heading: float, size: float) -> list[tuple[float, float]]:
    # heading is robot forward direction
    p1 = (cx + cos(heading) * size, cy + sin(heading) * size)
    p2 = (cx + cos(heading + 2.45) * size * 0.9, cy + sin(heading + 2.45) * size * 0.9)
    p3 = (cx + cos(heading - 2.45) * size * 0.9, cy + sin(heading - 2.45) * size * 0.9)
    return [p1, p2, p3]


def draw_frame(i: int, font: ImageFont.ImageFont) -> Image.Image:
    im = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(im)

    # Grid area
    dr.rectangle([GRID_X0, GRID_Y0, GRID_X1, GRID_Y1], fill=GRID_BG)
    for k in range(11):
        x = GRID_X0 + k * CELL
        y = GRID_Y0 + k * CELL
        dr.line([(x, GRID_Y0), (x, GRID_Y1)], fill=GRID_LINE, width=2)
        dr.line([(GRID_X0, y), (GRID_X1, y)], fill=GRID_LINE, width=2)

    # Circular path point
    a = 2 * pi * i / FRAMES
    nx = CENTER_CELL_X + RADIUS_CELL * cos(a)
    ny = CENTER_CELL_Y + RADIUS_CELL * sin(a)

    # Use tangent direction for heading (clockwise)
    na = 2 * pi * ((i + 1) % FRAMES) / FRAMES
    nx2 = CENTER_CELL_X + RADIUS_CELL * cos(na)
    ny2 = CENTER_CELL_Y + RADIUS_CELL * sin(na)

    px, py = to_px(nx, ny)
    px2, py2 = to_px(nx2, ny2)
    heading = atan2(py2 - py, px2 - px)

    tri = triangle_points(px, py, heading, CELL * 0.36)
    dr.polygon(tri, fill=ROBOT)

    # Panel
    dr.rounded_rectangle([PANEL_X0, PANEL_Y0, PANEL_X1, PANEL_Y1], radius=10, fill=PANEL_BG)

    grid_rx = int(round(nx))
    grid_ry = int(round(ny))
    dlabel = direction_label(px2 - px, py2 - py)

    lines = [
        f"Robot #1 : ({grid_rx}, {grid_ry}) {dlabel} active",
        "Latest event : move(circle)",
        "Scent count : 0",
        f"Replay frame : {i}",
        "Command log :",
        "World.scents (set) : []",
        "Ops: circle replay demo",
        "10x10 snapshot (R=robot, s=scent, .=empty)",
    ]

    # 10x10 ascii snapshot
    matrix = [["." for _ in range(10)] for _ in range(10)]
    if 0 <= grid_rx <= 9 and 0 <= grid_ry <= 9:
        # Visual y grows downward; snapshot uses top row first
        matrix[9 - grid_ry][grid_rx] = "R"

    for row in matrix:
        lines.append("".join(row))

    ty = PANEL_Y0 + 14
    for line in lines:
        dr.text((PANEL_X0 + 12, ty), line, fill=TEXT, font=font)
        ty += 24

    return im


def main() -> None:
    font = ImageFont.load_default()
    images = [draw_frame(i, font) for i in range(FRAMES)]
    images[0].save(
        OUT_PATH,
        save_all=True,
        append_images=images[1:],
        duration=70,
        loop=0,
        optimize=False,
        disposal=2,
    )
    print(f"Generated {OUT_PATH} with {FRAMES} frames")


if __name__ == "__main__":
    main()
