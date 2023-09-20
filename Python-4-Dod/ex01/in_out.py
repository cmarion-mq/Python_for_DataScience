def square(x: int | float) -> int | float:
    '''Take as argument an int or a float. Return the square of the argument'''
    try:
        return x * x
    except Exception as err:
        print(err)


def pow(x: int | float) -> int | float:
    '''Take as argument an int or a float. Return the Exponentiation of
    the argument by himself'''
    try:
        return x**x
    except Exception as err:
        print(err)


def outer(x: int | float, function) -> object:
    '''Take as argument a number and a function.
    Returns an object that when called returns the result of the arguments
    calculation.'''
    count = 0

    def inner() -> float:
        try:
            nonlocal count
            if count == 0:
                count = function(x)
            else:
                count = function(count)
            return count
        except Exception as err:
            return print(err)

    return inner
