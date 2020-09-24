import pyxel
import random
from math import sqrt

from .collision import Collision


class Body:
    """
    Representa uma partícula ou corpo rígido com velocidade e posição bem 
    definidas.

    Cada sub-classe de Body representa um tipo diferente de caixa de contorno.
    """

    # Propriedades genéricas
    @property
    def density(self):
        return self.mass / self.area if self.area else float('inf')

    def __init__(self, pos=(0, 0), vel=(0, 0), mass=1.0, color=0):
        self.position_x, self.position_y = map(float, pos)
        self.velocity_x, self.velocity_y = map(float, vel)
        self.mass = float(mass)
        self.color = color

        self.force_x = 0.0
        self.force_y = 0.0

    def area(self):
        return 0.0

    def apply_force(self, fx, fy):
        """
        Aplica força ao objeto.

        Este método é cumulativo e permite que várias forças sejam acumuladas
        ao mesmo objeto em cada passo de simulação.
        """
        self.force_x += fx
        self.force_y += fy        

    def update_velocity(self, dt):
        """
        Atualiza velocidades de acordo com as forças acumuladas até o presente
        frame.
        """
        acc_x = self.force_x / self.mass
        acc_y = self.force_y / self.mass
        
        self.velocity_x += acc_x * dt
        self.velocity_y += acc_y * dt

        self.force_x = self.force_y = 0.0

    def update_position(self, dt):
        """
        Atualiza posições de acordo com as velocidades.
        """
        self.position_x += self.velocity_x * dt
        self.position_y += self.velocity_y * dt

    def draw(self):
        """
        Desenha figura na tela.
        """
        pyxel.pset(self.position_x, self.position_y, self.color)

    #
    # Calcula colisões com outras figuras geométricas.
    #
    def get_collision(self, other: 'Body') -> 'Collision':
        """
        Verifica se há colisão com outro objeto e retorna um objeto de colisão 
        ou None caso não exista superposição.
        """ 
        raise NotImplementedError(type(self), type(other))

    def get_collision_circle(self, other: 'Circle'):
        """
        Verifica colisão com círculos.
        """
        raise NotImplementedError

    def get_collision_aabb(self, other):
        """
        Verifica colisão com AABBs.
        """
        raise NotImplementedError

    def get_collision_poly(self, other):
        """
        Verifica colisão com Polígonos.
        """
        raise NotImplementedError

    def get_collision_pill(self, other):
        """
        Verifica colisão com Pílulas.
        """
        raise NotImplementedError



class Circle(Body):
    """
    Corpo físico com caixa de contorno circular.
    """
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


class AABB(Body):
    """
    Objeto com caixa de contorno retangular e alinhada aos eixos. 
    """

    @property
    def left(self):
        return self.position_x - self.width / 2

    @property
    def right(self):
        return self.position_x + self.width / 2

    @property
    def bottom(self):
        return self.position_y - self.height / 2

    @property
    def top(self):
        return self.position_y + self.height / 2

    def __init__(self, left, bottom, right, top, *args, **kwargs):
        assert left <= right
        assert bottom <= top
        self.width = right - left + 0.0
        self.height = top - bottom + 0.0
        x = (left + right) / 2.0
        y = (top + bottom) / 2.0
        super().__init__((x, y), *args, **kwargs)

    def draw(self):
        pyxel.rect(self.left, self.bottom, self.width, self.height, self.color)

    def get_collision(self, other):
        return other.get_collision_aabb(self)

    def get_collision_aabb(self, other):
        xa = max(self.left, other.left)
        xb = min(self.right, other.right)
        dx = xb - xa 

        ya = max(self.bottom, other.bottom)
        yb = min(self.top, other.top)
        dy = yb - ya

        if dy >= 0 and dx >= 0:
            pos = [xm, ym] = (xa + xb) / 2, (ya + yb) / 2
            if dx > dy:
                normal = (0, 1 if self.left < xm else -1)
            else:
                normal = (1 if self.bottom < ym else -1, 0)
            return Collision(self, other, pos, normal)


class Segment(Body):
    """
    Objeto com caixa de contorno em forma de pílula, ou seja, um segmento de reta com 
    um determinado raio de colisão. 
    """
    NotImplemented


class Poly(Body):
    """
    Objeto com caixa de contorno poligonal e alinhada aos eixos. 
    """
    NotImplemented
