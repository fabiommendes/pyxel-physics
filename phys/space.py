from typing import List

from .body import Body, Circle, AABB, Poly, Segment 
from .vec2d import Vec2d, VecLike


class Space:
    """
    Representa um grupo de objetos que interagem entre si.
    """
    
    def __init__(self):
        self.bodies = []
    
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
        
    def add_aabb(self, *args, **kwargs) -> 'Circle':
        """
        Cria AABB e adiciona ao espaço.
        """
        return self._add_object(AABB, *args, **kwargs)

    def add_poly(self, *args, **kwargs) -> 'Circle':
        """
        Cria polígono e adiciona ao espaço.
        """
        return self._add_object(Poly, *args, **kwargs)

    def add_segment(self, *args, **kwargs) -> 'Circle':
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
        for body in self.bodies:
            body.update_velocity(dt)

        # Encontra colisões
        collisions = []
        for i, obj_a in enumerate(self.bodies):
            for obj_b in self.bodies[i+1:]:
                col = obj_a.get_collision(obj_b)
                if col is not None:
                    collisions.append(col)

        # Resolve as colisões
        for collision in collisions:
            collision.resolve_collision()

        for body in self.bodies:
            body.update_position(dt)

    #
    # Desenha
    #
    def draw(self):
        for body in self.bodies:
            body.draw()
