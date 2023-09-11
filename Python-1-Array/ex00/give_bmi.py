def bmi_calculate(height: int | float, weight: int | float) -> int | float:
    '''
    Calculate the BMI.
    '''
    try:
        return (weight / (height * height))
    except Exception as err:
        print('An error occured', err)


def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    '''
    Calculate the BMI list from height and weight list
    '''
    try:
        if (len(height) != len(weight)):
            return print('AssertionError: lists have different sizes')
        height_weight = zip(height, weight)
        if len([val for sublist in height_weight for val in sublist
                if not isinstance(val, (float, int))]):
            return print('AssertionError: the arguments are bad')
        return [bmi_calculate(h, w) for h, w in zip(height, weight)]
    except Exception as err:
        print('An error occured', err)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    List the BMI which are or not under a limit
    '''
    if not bmi or not isinstance(limit, (float, int)):
        return print('AssertionError: the arguments are bad')
    return [val > limit for val in bmi]
