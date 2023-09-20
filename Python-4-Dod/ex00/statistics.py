def ft_mean(args: list[int | float]):
    '''Take as argument a list of int or float.
    Calclate and display the mean of the argument'''
    try:
        print("mean :", sum(args) / len(args))
    except Exception:
        print("ERROR")


def ft_median(args: list[int | float]):
    '''Take as argument a list of int or float.
    Calclate and display the median of the argument'''
    try:
        sorted_args = sorted(args)
        args_len = len(args)
        if len(args) % 2 == 0:
            print("median :",
                  (sorted_args[int((args_len / 2) + 0.5)]
                   + sorted_args[int((args_len / 2) - 0.5)]) / 2)
        else:
            print("median :", sorted_args[int(len(args) / 2)])
    except Exception:
        print("ERROR")


def ft_quartile(args: list[int | float]):
    '''Take as argument a list of int or float.
    Calclate and display the 25% and 75% quartile of the argument'''
    try:
        sorted_args = sorted(args)
        print("quartile :", [float(sorted_args[int(len(args) / 4)]),
                             float(sorted_args[int(3 * len(args) / 4)])])
    except Exception:
        print("ERROR")


def ft_std(args: list[int | float]):
    '''Take as argument a list of int or float.
    Calclate and display the standard deviation of the argument'''
    try:
        mean = sum(args) / len(args)
        std_sum = 0
        for val in args:
            std_sum = std_sum + (val - mean)**2
        print("std :", (std_sum / len(args))**0.5)
    except Exception:
        print("ERROR")


def ft_var(args: list[int | float]):
    '''Take as argument a list of int or float.
    Calclate and display the variance of the argument'''
    try:
        mean = sum(args) / len(args)
        std_sum = 0
        for val in args:
            std_sum = std_sum + (val - mean)**2
        print("var :", (std_sum / len(args)))
    except Exception:
        print("ERROR")


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Take as first argumant an undefined length of elements in a list,
    and as second argument an undefined length of elements in a dictionnary.
    Calculate and display the variance of the argument'''
    for key, value in kwargs.items():
        match value:
            case "mean":
                ft_mean(args)
            case "median":
                ft_median(args)
            case "quartile":
                ft_quartile(args)
            case "std":
                ft_std(args)
            case "var":
                ft_var(args)
