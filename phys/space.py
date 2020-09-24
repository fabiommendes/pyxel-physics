from typing import List

import pyxel

from .body import Body
from .circle import Circle
from .aabb import AABB
from .poly import Poly
from .segment import Segment
from .vec2d import Vec2d, VecLike


class Space:
    """
    Representa um grupo de objetos que interagem entre si.
    """

    def __init__(self):
        self.time = 0.0
        self.current_time_step = 0.0
        self.bodies = []

    def __contains__(self, body):
        return body in self.bodies

    #
    # Criação e remoção de objetos
    #
    def add(self, body):
        """
        Adiciona objeto ao espaço.
        """
        self.bodies.append(body)

    def _add_object(self, cls, *args, **kwargs) -> Body:
        obj = cls(*args, **kwargs)
        self.add(obj)
        return obj

    def add_circle(self, *args, **kwargs) -> Circle:
        """
        Cria círculo e adiciona ao espaço.
        """
        return self._add_object(Circle, *args, **kwargs)

    def add_aabb(self, *args, **kwargs) -> "Circle":
        """
        Cria AABB e adiciona ao espaço.
        """
        return self._add_object(AABB, *args, **kwargs)

    def add_poly(self, *args, **kwargs) -> "Circle":
        """
        Cria polígono e adiciona ao espaço.
        """
        return self._add_object(Poly, *args, **kwargs)

    def add_segment(self, *args, **kwargs) -> "Circle":
        """
        Cria segmento e adiciona ao espaço.
        """
        return self._add_object(Segment, *args, **kwargs)

    def remove(self, obj):
        """
        Remove objeto da simulação.
        """
        raise NotImplementedError

    # Verifica colisões e pontos
    def point_query(self, vec: VecLike) -> List[Body]:
        """
        Retorna a lista de todos objetos que tocam o ponto dado.
        """
        raise NotImplementedError

    #
    # Simulação
    #
    def step(self, dt):
        """
        Executa um passo de simulação.
        """
        self.current_time_step = dt

        # Atualiza as velocidades dos corpos em função das forças acumuladas.
        for body in self.bodies:
            body.update_velocity(dt)

        # Resolve as colisões.
        for collision in self.get_collisions():
            collision.resolve()

        # Finalmente atualiza as posições.
        for body in self.bodies:
            body.update_position(dt)

        self.time += dt

    def get_collisions(self):
        """
        Retorna sequência de colisões para o frame.
        """
        for i, obj_a in enumerate(self.bodies):
            for obj_b in self.bodies[i + 1 :]:
                col = obj_a.get_collision(obj_b)
                if col is not None:
                    yield col

    #
    # Outras funções
    #
    def draw(self, *, background=None):
        """
        Desenha o espaço chamando a função .draw() de cada elemento do espaço.
        """

        if background is not None:
            pyxel.cls(background)

        for body in self.bodies:
            body.draw()
