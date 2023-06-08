"""Defines the iteration step and chaotic map proposed."""

from typing import Tuple
from chaos_maps import ChaoticMap
import numpy 

def map_iteration(x: Tuple[float], parameters: Tuple[float]) -> Tuple[float]:
    """Defines the iteration step and chaotic map proposed.
    
    Parameters
    ----------
    x : Tuple[float]
        The variables of the system.
    parameters : Tuple[float]
        The parameters of the system.

    Returns
    -------
    Tuple[float]
        The next trajectory point.
    """

    x1, x2 = x
    Z, a, b = parameters

    x1_next = x2

    term_1 = Z * a * numpy.tanh(x1)
    term_2 = (1-Z) * b * numpy.tanh(x2)

    x2_next = numpy.fmod(term_1 + term_2, 1)

    return x1_next, x2_next
    
chaotic_map = ChaoticMap(map_iteration)
