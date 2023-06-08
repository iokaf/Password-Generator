"""This module defines the proposed pseudo random bit generator."""

def convert_to_int(x: float):
    """This function converts a float number to an integer.

    Notes:
    ------
    The method does the following:
    1. Multiplies the float by 10**14
    2. Takes the floor of the result
    3. Takes the remainder of the division by 128
    4. Converts the result to its binary representation
    5. Flips the digits of the binary representation
    6. Converts the result to an integer

    Parameters
    ----------
    x : float
        The number to be converted.

    Returns
    -------
    int
        The converted number.
    """

    int_value = int(x * 10**14)
    remainder = int_value % 128
    binary = bin(remainder)[2:]
    flipped = binary[::-1]
    return int(flipped, 2)
    

def PRBG(x: float, y: float):
    """This function defines the proposed pseudo random bit generator.

    Notes:
    ------
    The method does the following:
    1. Converts the first variable to an integer
    2. Converts the second variable to an integer
    3. Calculates the XOR of the two integers
    4. Returns the result

    Parameters
    ----------
    x : float
        The first variable of the system.
    y : float
        The second variable of the system.

    Returns
    -------
    Tuple[float]
        The next trajectory point.
    """

    int_x = convert_to_int(x)
    int_y = convert_to_int(y)

    return int_x ^ int_y
    