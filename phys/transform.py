from typing import Union, Tuple
from numbers import Number
from math import sqrt, pi
from functools import singledispatch

from .vec2d import Vec2d, VecLike, asvec2d
from .mat22 import Mat2, asmat2

RADS_TO_DEGREES = 180 / pi
DEGREES_TO_RADS = pi / 180


class Transform:
    """
    Transformação afim em 2D.

    Multiplicação de transformações afins é entendida como encadeamento de transformações.
    Uma transformação afim multiplicada por um vetor realiza a transformação neste vetor.

    A transformação é criada a partir dos atributos:
        
        [[a, c, tx],
         [b, d, ty]]
    """

    # Propriedades e atributos
    a: float
    b: float
    c: float
    d: float
    tx: float
    ty: float

    @property
    def mat2(self):
        """
        Matriz implícita na transformação afim.
        """
        raise NotImplementedError

    @property
    def vec2(self):
        """
        Vetor de translação da transformação afim.
        """
        raise NotImplementedError

    # Construtores alternativos
    @classmethod
    def affine(cls, mat=None, translation=None):
        """
        Cria transformação afim a partir da matriz de transformação linear e 
        um vetor de deslocamento
        """
        return cls.scale(1, 1)

    @classmethod
    def identity(cls):
        """
        Cria transformação de identidade.
        """
        return cls.scale(1, 1)

    @classmethod
    def rotation(cls, angle):
        """
        Cria uma transformação de rotação (ângulo em radianos).
        """
        raise NotImplementedError

    @classmethod
    def rotation_degrees(cls, angle):
        """
        Cria uma transformação de rotação (ângulo em graus).
        """
        return cls.rotation(angle * DEGREES_TO_RADS)

    @classmethod
    def scale(cls, scale_x, scale_y=None):
        """
        Cria transformação de escala.
        """
        raise NotImplementedError

    @classmethod
    def similarity(cls, scale=None, angle=None, angle_degrees=None, translation=None):
        """
        Cria transformação de similaridade a partir de operação fundamental.
        """
        raise NotImplementedError

    def __init__(self, a=1, b=0, c=0, d=1, tx=0, ty=0):
        self.a = a + 0.0
        self.b = b + 0.0
        self.c = c + 0.0
        self.d = d + 0.0
        self.tx = tx + 0.0
        self.ty = ty + 0.0

    def __mul__(self, other):
        raise NotImplementedError

    def __rmul__(self, other):
        raise NotImplementedError

    # Comparações
    def __eq__(self, other):
        raise NotImplementedError

    def __neq__(self, other):
        raise NotImplementedError

    # Comportamento de sequências
    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, idx):
        raise NotImplementedError

    def __setitem__(self, idx, value):
        raise NotImplementedError

    # Métodos da classe
    def copy(self):
        """
        Retorna cópia da transformação afim.
        """
        raise NotImplementedError

    def rotate(self, angle: float):
        """
        Rotaciona vetor pelo ângulo em radianos.
        """
        raise NotImplementedError

    def rotate_degrees(self, angle: float):
        """
        Rotaciona vetor pelo ângulo em graus.
        """
        self.rotate(angle * DEGREES_TO_RADS)

    def rotated(self, angle: float) -> "Transform":
        """
        Cria nova transformação afim rotacionado ângulo em radianos.
        """
        new = self.copy()
        new.rotate(angle)
        return new

    def rotated_degrees(self, angle: float) -> "Transform":
        """
        Cria nova transformação afim rotacionado ângulo em graus.
        """
        return self.rotated(angle * DEGREES_TO_RADS)

    def transform(self, obj):
        """
        Transforma objeto por transformação  afim.
        """
        raise NotImplementedError

    def transformed(self, obj):
        """
        Retorna cópia de objeto transformado objeto por transformação afim.
        """
        raise NotImplementedError

    def translate(self, vec: VecLike):
        """
        Acrescenta vetor de translação à transformação.
        """
        raise NotImplementedError

    def translated(self, vec: VecLike):
        """
        Retorna nova transformação transladada por vetor.
        """
        new = self.copy()
        new.translate(vec)
        return new


#
# Funções auxiliares
#
def astransform(obj) -> "Transform":
    """
    Converte objeto para Transform, caso não seja. 
    """
    if isinstance(obj, Transform):
        return obj
    elif isinstance(obj, Mat2):
        return Transform.affine(obj, (0, 0))
    elif isinstance(obj, (tuple, list, Vec2d)):
        return Transform.affine(Mat2.identity(), asvec2d(obj))
    kind = type(obj).__name__  # Extrai nome do tipo de obj.
    raise TypeError(f"não pode converter {kind} em Transform")


@singledispatch
def transformed(obj, transform: Transform):
    """
    Retorna cópia de objeto transformado pela transformação afim dada.
    """
    new = obj.copy()
    transform(new)
    return new


@singledispatch
def transform(obj, transform: Transform):
    """
    Transforma objeto pela transformação afim dada.
    """
    raise NotImplementedError
