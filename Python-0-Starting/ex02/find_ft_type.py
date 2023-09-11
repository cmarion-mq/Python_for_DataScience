def all_thing_is_obj(object: any) -> int:
    type_ = type(object)
    match type_.__name__:
        case 'list' | 'tuple' | 'set' | 'dict':
            print(f'{type_.__name__.capitalize()} : {type_}')
        case 'str':
            print(f'Brian is in the kitchen : {type_}')
        case _:
            print('Type not found')
    return 42
