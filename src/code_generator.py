"""This module implements conversion of user inputs to system parameters."""
from typing import Dict

import numpy

def inverse_ascii_order_sum(
        word: str, 
        factor: float = 1,
        exponent: bool = False    
    ) -> int:
    """Calculates the sum of the ASCII codes of the characters in the word times
    the position of the character in the word.

    Parameters
    ----------
    word : str
        The word.

    Returns
    -------
    int
        The sum of the ASCII codes of the characters in the word.
    """
    
    sum = 0
    for i, char in enumerate(word):
        if exponent:
            sum +=  (factor /((i+1) * ord(char))) ** numpy.fmod((i+1), 10)
        else:
            sum +=  factor /((i+1) * ord(char))

    return sum

def get_a_one(word: str) -> float:
    """Converts the user name to the a1 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The a1 system parameter.
    """

    inverse_letter_sum = inverse_ascii_order_sum(word, factor=1) 

    return 5 + 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_a_two(word: str) -> float:
    """Converts the platform name to the a2 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The a2 system parameter.
    """

    inverse_letter_sum = inverse_ascii_order_sum(word, factor=5) 

    return 10 + 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_b_one(word: str) -> float:
    """Converts the favorite animal to the b1 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The b1 system parameter.
    """

    inverse_letter_sum = inverse_ascii_order_sum(word, factor=2) 

    return 5 + 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_b_two(word: str) -> float:
    """Converts the mother's family name to the b2 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The b2 system parameter.
    """
    inverse_letter_sum = inverse_ascii_order_sum(word, factor=2, exponent=True) 

    return 10 + 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_Z_one(word: str) -> float:
    """Converts the username to the Z1 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The Z1 system parameter.
    """

    inverse_letter_sum = inverse_ascii_order_sum(word, factor=3) 

    return 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_Z_two(word: str) -> float:
    """Converts the platform name to the Z2 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        The Z2 system parameter.
    """

    inverse_letter_sum = inverse_ascii_order_sum(word, factor=4) 

    return 1e-06 + numpy.fmod(inverse_letter_sum, 1)

def get_initial_condition(word: str) -> float:
    """Converts the favorite animal to the x0 system parameter.

    Parameters
    ----------
    word : str
        The word used to produce the parameter.

    Returns
    -------
    float
        An initial condition for the system.
    """

    inverse_sum = 0

    for i, char in enumerate(word):

        term = 2 / (i+1) * ord(char)

        rem = numpy.fmod(term, 1)

        exponent = numpy.fmod(i+1, 10)

        inverse_sum += rem ** exponent

    return 1e-06 + inverse_sum


def create_parameters(
        user_inputs: Dict[str, str]
    ) -> Dict[str, float]:
    """Converts user inputs to system parameters.

    Parameters
    ----------
    user_inputs : Dict[str, str]
        The user inputs.

    Returns
    -------
    Dict[str, float]
        The system parameters.
    """

    un = user_inputs["username"]
    plt = user_inputs["platform"]
    sq1 = user_inputs["favorite_animal"]
    sq2 = user_inputs["mother_family_name"]
    sq3 = user_inputs["first_teacher_name"]

    return {
        "a1": get_a_one(un),
        "a2": get_a_two(sq3),
        "b1": get_b_one(plt),
        "b2": get_b_two(plt),
        "Z1": get_Z_one(sq1),
        "Z2": get_Z_two(sq2),
        "x0": get_initial_condition(un),
        "x1": get_initial_condition(sq1),
        "y0": get_initial_condition(sq2),
        "y1": get_initial_condition(sq3),
    }






