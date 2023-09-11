import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Take as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start
    and end arguments.
    '''
    try:

        if not isinstance(family, list) or len(np.shape(family)) != 2:
            return print("AssertionError: First argument has to be a 2D array")
        if not all(isinstance(i, int) for i in [start, end]):
            return print("AssertionError: Second and third arguments"
                         " have to be integer")
        print("My shape is :", np.shape(family))
        new_family = family[start:end]
        print("My new shape is :", np.shape(new_family))
        return new_family
    except Exception as err:
        print('An error occured', err)
