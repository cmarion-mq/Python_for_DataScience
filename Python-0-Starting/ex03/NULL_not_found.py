def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f'Nothing: {object} {type(object)}')
            return 0
        elif isinstance(object, bool) and not object:
            print(f'Fake: {object} {type(object)}')
            return 0
        elif object != object:
            print(f'Cheese: {object} {type(object)}')
            return 0
        elif object == 0:
            print(f'Zero: {object} {type(object)}')
            return 0
        elif object == '':
            print(f'Empty: {object} {type(object)}')
            return 0
        else:
            print('Type not Found')
            return 1
    except NameError:
        return 1
