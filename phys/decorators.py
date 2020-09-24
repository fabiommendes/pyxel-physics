def vector_argument(func):
    """
    Decorador que transforma função que recebe um vetor como único argumento 
    posicional (e qualquer número de argumentos passados por nome) e retorna 
    uma função que aceita tanto um vetor ou tupla como único argumento ou 
    dois argumentos posicionais com cada coordenada.

    Examples:
    >>> @vector_argument
    ... def length_sqr(vec):
    ...     return vec.x**2 + vec.y**2

    Agora a função aceita várias assinaturas:
    >>> length_sqr(Vec2d(3, 4))
    25.0
    >>> length_sqr((3, 4))
    25.0
    >>> length_sqr(3, 4)
    25.0
    """

    ...  # Implementar!
    return func


def vector_argument_method(method):
    """
    Similar à função :func:`vector_argument`, mas aplicável a métodos
    de classe que recebem "self" como primeiro argumento.
    """

    ...  # Implementar!
    return method
