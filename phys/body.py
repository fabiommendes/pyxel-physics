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
    position_x: float = None
    position_y: float = None
    
    @property
    def area(self):
        name = type(self).__name__
        raise NotImplementedError(f"Corpo {name} não implementa área")

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

    def get_collision_segment(self, other):
        """
        Verifica colisão com Pílulas.
        """
        raise NotImplementedError
