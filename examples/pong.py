import random
import pyxel
from phys import Space, AABB


# Constantes
SPEED = 40
VELOCITIES = [(x, y) for x in [-SPEED, SPEED] for y in [-SPEED, SPEED]]
STEP = 0.75
FPS = 60
dt = 1 / FPS

# Elementos dinâmicos
h = 8
space = Space()
player1 = space.add_aabb(5, 45 - h, 8, 45 + h, color=pyxel.COLOR_WHITE)
player2 = space.add_aabb(112, 45 - h, 115, 45 + h, color=pyxel.COLOR_WHITE)
ball = space.add_aabb(58, 43, 62, 47, color=pyxel.COLOR_RED)

# Margens
margin_bottom = space.add_aabb(0, 90, 120, 100, mass="inf")
margin_top = space.add_aabb(0, -10, 120, 0, mass="inf")


def update():
    if pyxel.btn(pyxel.KEY_UP):
        player2.position_y -= STEP
    if pyxel.btn(pyxel.KEY_DOWN):
        player2.position_y += STEP
    if pyxel.btn(pyxel.KEY_W):
        player1.position_y -= STEP
    if pyxel.btn(pyxel.KEY_S):
        player1.position_y += STEP
    if pyxel.btnp(pyxel.KEY_SPACE):
        ball.velocity_x, ball.velocity_y = random.choice(VELOCITIES)
    if pyxel.btnp(pyxel.KEY_R):
        ball.velocity_x, ball.velocity_y = (0, 0)
        ball.position_x, ball.position_y = (60, 45)

    space.step(dt)


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    space.draw()


pyxel.init(120, 90, fps=FPS, caption="Pong")
pyxel.run(update, draw)
