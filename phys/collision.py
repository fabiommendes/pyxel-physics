import pyxel


class Collision:
    """
    Representa uma colisão 
    """
    def __init__(self, obj_a, obj_b, pos, normal):
        self.obj_a = obj_a
        self.obj_b = obj_b
        self.position_x, self.position_y = pos
        self.normal_x, self.normal_y = normal

    def resolve_collision(self):
        if self.normal_x == 0:
            self.obj_a.velocity_y *= -1
            self.obj_b.velocity_y *= -1
        elif self.normal_y == 0:
            self.obj_a.velocity_x *= -1
            self.obj_b.velocity_x *= -1
        else:
            self.obj_a.velocity_x = 0
            self.obj_a.velocity_y = 0
            self.obj_b.velocity_x = 0
            self.obj_b.velocity_y = 0
            self.obj_a.color = pyxel.COLOR_RED
            self.obj_b.color = pyxel.COLOR_RED

    def draw(self, color=pyxel.COLOR_RED):
        x, y = self.position_x, self.position_y
        nx, ny = self.normal_x, self.normal_y
        pyxel.line(x, y, x + nx, y + ny, color)
        pyxel.circ(x, y, 1, color)
        