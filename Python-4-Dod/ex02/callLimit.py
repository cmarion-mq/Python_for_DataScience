def callLimit(limit: int):
    '''Take as argument a call limit of another function and blocks
    its execution above a limit.'''
    try:
        count = 0

        def callLimiter(function):
            def limit_function(*args: any, **kwds: any):
                nonlocal count
                if count >= limit:
                    print("Error:", function, "call too many times")
                else:
                    function()
                count += 1
            return limit_function
        return callLimiter
    except Exception as err:
        print(err)
