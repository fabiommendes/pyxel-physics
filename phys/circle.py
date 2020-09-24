from math import pi, sqrt

import pyxel

from .body import Body
from .collision import Collision


class Circle(Body):
    """
    Corpo físico com caixa de contorno circular.
    """

    @property
    def area(self):
        return pi * self.radius ** 2

    def __init__(self, radius, *args, **kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)
    
    def draw(self):
        pyxel.circ(self.position_x, self.position_y, self.radius, self.color)

    def get_collision(self, other):
        return other.get_collision_circle(self)

    def get_collision_circle(self, other):
        dx = self.position_x - other.position_x
        dy = self.position_y - other.position_y
        distance = sqrt(dx**2 + dy**2)
        
        if distance <= self.radius + other.radius:
            return Collision(self, other, (0, 0), (0, 0))
        else:
            return None


