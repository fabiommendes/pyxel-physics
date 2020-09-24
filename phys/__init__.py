"""
Physics module for the Pyxel engine.
"""
__version__ = "0.0.1b"

from .body import Body, Circle, AABB, Segment, Poly
from .space import Space
from .collision import Collision
from .vec2d import Vec2d, VecLike, asvec2d
from .mat22 import Mat2, MatLike, asmat2
from .transform import Transform, astransform
