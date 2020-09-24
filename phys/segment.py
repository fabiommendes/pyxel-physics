import pyxel

from .body import Body
from .collision import Collision


class Segment(Body):
    """
    Objeto com caixa de contorno em forma de pílula, ou seja, um segmento de reta com 
    um determinado raio de colisão. 
    """

    @property
    def area(self):
        raise NotImplementedError

    @property
    def position_x(self):
        return (self.a_x + self.b_x) / 2

    @position_x.setter
    def position_x(self, value):
        dx = value - self.position_x
        self.a_x += dx
        self.b_x += dx

    @property
    def position_y(self):
        raise NotImplementedError

    @position_y.setter
    def position_y(self, value):
        raise NotImplementedError

    def __init__(self, a, b, radius, *args, **kwargs):
        self.a_x, self.a_y = a
        self.b_x, self.b_y = b
        self.radius = float(self.radius)
        super().__init__(None, *args, **kwargs)

    def draw(self):
        raise NotImplementedError

    def update_position(self, dt):
        raise NotImplementedError

    def get_collision(self, other):
        raise NotImplementedError

    def get_collision_aabb(self, other):
        raise NotImplementedError
