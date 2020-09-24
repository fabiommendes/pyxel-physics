import pyxel


class Collision:
    """
    Representa uma colisão 
    """

    @property
    def bodies(self):
        return [self.body_a, self.body_b]

    def __init__(self, obj_a, obj_b, pos, normal):
        self.body_a = obj_a
        self.body_b = obj_b
        self.position_x, self.position_y = pos
        self.normal_x, self.normal_y = normal

    def resolve(self):
        """
        Calcula e aplica impulsos de colisão entre dois objetos. 
        """
        self.body_a.velocity_x = 0
        self.body_a.velocity_y = 0
        self.body_b.velocity_x = 0
        self.body_b.velocity_y = 0
        self.body_a.color = pyxel.COLOR_RED
        self.body_b.color = pyxel.COLOR_RED

    def draw(self, color=pyxel.COLOR_RED):
        """
        Desenha ponto e vetores relevantes para a colisão.
        """
        x, y = self.position_x, self.position_y
        nx, ny = self.normal_x, self.normal_y
        pyxel.line(x, y, x + nx, y + ny, color)
        pyxel.circ(x, y, 1, color)
