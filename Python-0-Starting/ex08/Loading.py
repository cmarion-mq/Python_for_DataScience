def ft_tqdm(lst: range) -> None:
    '''
    Display a progress bar from a range
    '''
    if not isinstance(lst, range):
        return print('AssertionError: the argument is not a range')
    for n in lst:
        try:
            rate = n / lst[-1]
            progress_bar = (round(rate * 60) * "=") + '>' \
                + (round((1 - rate) * 60) * " ")
            print(f"{round(rate * 100)}%|[{progress_bar}]| "
                  f"{n + 1}/{lst[-1] + 1}", end="\r")
            yield n
        except Exception as err:
            print('An error occured', err)
