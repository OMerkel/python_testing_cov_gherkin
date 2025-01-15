""" A simple math module """


def my_add(x: float, y: float) -> float:
    """ Add two floats representing sizes of a shape

    mind: There is no negative size for a shape

    params:
        x: float representing the size of a shape
        y: float representing the size of a shape

    returns the sum of the two numbers representing sizes of a shape
    returns NaN if any size is negative
    """
    if x < 0 or y < 0:
        return float('nan')
    return x + y
