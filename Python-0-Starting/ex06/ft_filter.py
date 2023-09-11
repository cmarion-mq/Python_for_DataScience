def ft_filter(function, iterable: iter):
    '''
    Construct an iterator from those elements of iterable
    for which function is true. iterable may be either a sequence,
    a container which supports iteration, or an iterator.
    If function is None, the identity function is assumed,
    that is all elements of iterable that are false are removed.

    '''
    try:
        if function is None:
            return [x for x in iterable if x]
        else:
            return [x for x in iterable if function(x)]
    except Exception as err:
        print('An error occured', err)
