import random
from math import sqrt

import pyxel
from phys import Space


N = 5
N_STARS = 50
FPS = 60
SPEED = 30
COLORS = [i for i in range(16) if i not in (pyxel.COLOR_BLACK, pyxel.COLOR_WHITE)]
STARS = [(random.uniform(0, 180), random.uniform(0, 120)) for i in range(N_STARS)]
dt = 1 / FPS
sp = Space()

for _ in range(N):
    sp.add_circle(
        radius=random.uniform(2, 3),
        pos=(random.uniform(0, 180), random.uniform(0, 120)),
        vel=(random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)),
        color=random.choice(COLORS),
    )
sp.add_circle(radius=6, pos=(90, 60), color=pyxel.COLOR_RED, mass=10)


def apply_gravity(A, B, cte=1e4):
    dx = A.position_x - B.position_x
    dy = A.position_y - B.position_y
    r = sqrt(dx**2 + dy**2)
    dx /= r
    dy /= r

    F = -cte / (r + 10)**2 
    Fx = dx * F
    Fy = dy * F

    A.apply_force(Fx, Fy)
    B.apply_force(-Fx, -Fy) 


def apply_force(obj, x, y, cte=50, gamma=0.5):
    dx = obj.position_x - x
    dy = obj.position_y - y
    r = sqrt(dx**2 + dy**2)
    dx /= r
    dy /= r

    Fx = -cte * obj.mass * dx - gamma * obj.mass * obj.velocity_x
    Fy = -cte * obj.mass * dy - gamma * obj.mass * obj.velocity_y

    obj.apply_force(Fx, Fy)


def update():
    # Força da gravidade
    for i, A in enumerate(sp.bodies):
        for B in sp.bodies[i + 1:]:
            apply_gravity(A, B)

    # Força atrativa controlada pelo mouse
    if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
        for body in sp.bodies:
            apply_force(body, pyxel.mouse_x, pyxel.mouse_y)

    sp.step(dt)


def draw_stars():
    pyxel.cls(pyxel.COLOR_BLACK)

    if pyxel.frame_count % 8 == 0:
        star_field[:] = stars_field_commands()
    for args in star_field:
        pyxel.pset(*args)


def stars_field_commands():
    colors = [pyxel.COLOR_WHITE, pyxel.COLOR_GRAY]

    for i, (x, y) in enumerate(STARS):
        r = random.random()
        if r < 0.7: 
            yield (x, y, colors[i % 2])
        elif r < 0.85: 
            yield (x, y, pyxel.COLOR_GRAY)
        elif r < 0.9: 
            yield (x, y, pyxel.COLOR_YELLOW)
        elif r < 0.91:
            for a, b in [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]:
                yield (x + a, y + b, pyxel.COLOR_WHITE)


def draw():
    draw_stars()
    if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 2, pyxel.COLOR_RED)
    else:
        pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, pyxel.COLOR_WHITE)
    sp.draw()


star_field = list(stars_field_commands())
pyxel.init(180, 120, fps=FPS)
pyxel.run(update, draw)
