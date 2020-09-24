import pyxel

from .body import Body
from .collision import Collision


class Poly(Body):
    """
    Objeto com caixa de contorno poligonal e alinhada aos eixos. 
    """

    @property
    def area(self):
        raise area(self._vertices)

    @property
    def position_x(self):
        return center_of_gravity(self._vertices)

    @position_x.setter
    def position_x(self, value):
        dx = value - self.position_x
        self._vertices = [v + (dx, 0) for v in self._vertices]

    @property
    def position_y(self):
        raise NotImplementedError

    @position_y.setter
    def position_y(self, value):
        raise NotImplementedError

    def __init__(self, vertices, *args, **kwargs):
        self._vertices = list(vertices)
        super().__init__((self.position_x, self.position_y), *args, **kwargs)

    def get_vertices(self):
        return self._vertices

    def draw(self):
        raise NotImplementedError

    def update_position(self, dt):
        raise NotImplementedError

    def get_collision(self, other):
        raise NotImplementedError

    def get_collision_aabb(self, other):
        raise NotImplementedError


def area(vertices):
    """
    Calcula área de polígono a partir da lista de vértices.

    Assume polígono convexo enrolado de forma anti-horária.
    """
    raise NotImplementedError


def center_of_gravity(vertices):
    """
    Calcula centro de gravidade de polígono a partir da lista de vértices.

    Assume polígono convexo enrolado de forma anti-horária.
    """
    raise NotImplementedError
