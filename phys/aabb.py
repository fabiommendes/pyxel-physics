import pyxel

from .body import Body
from .collision import Collision


class AABB(Body):
    """
    Objeto com caixa de contorno retangular e alinhada aos eixos. 
    """

    @property
    def area(self):
        raise NotImplementedError

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        raise NotImplementedError

    @property
    def position_x(self):
        return (self.left + self.right) / 2

    @position_x.setter
    def position_x(self, value):
        dx = value - self.position_x
        self.left += dx
        self.right += dx

    @property
    def position_y(self):
        raise NotImplementedError

    @position_y.setter
    def position_y(self, value):
        raise NotImplementedError

    def __init__(self, left, bottom, right, top, *args, **kwargs):
        assert left <= right
        assert bottom <= top
        self.left, self.right, self.bottom, self.top = left, right, bottom, top
        super().__init__((self.position_x, self.position_y), *args, **kwargs)

    def draw(self):
        raise NotImplementedError

    def update_position(self, dt):
        raise NotImplementedError

    def get_collision(self, other):
        raise NotImplementedError

    def get_collision_aabb(self, other):
        raise NotImplementedError
