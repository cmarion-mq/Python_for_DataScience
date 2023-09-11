from matplotlib import pyplot as plt
import numpy as np


def ft_invert(array) -> list:
    '''
    Inverts the color of the image received.
    '''
    if not isinstance(array, np.ndarray):
        return print("Your argument has to be an array")
    ret = [255, 255, 255] - array
    plt.imshow(ret)
    plt.show()
    return ret


def ft_red(array) -> list:
    '''
    Keep red color of the image received.
    '''
    if not isinstance(array, np.ndarray):
        return print("Your argument has to be an array")
    ret = array * [1, 0, 0]
    plt.imshow(ret)
    plt.show()
    return ret


def ft_green(array) -> list:
    '''
    Keep green color of the image received.
    '''
    if not isinstance(array, np.ndarray):
        return print("Your argument has to be an array")
    ret = array.copy()
    ret[..., 0] = 0
    ret[..., 2] = 0
    plt.imshow(ret)
    plt.show()
    return ret


def ft_blue(array) -> list:
    '''
    Keep blue color of the image received.
    '''
    if not isinstance(array, np.ndarray):
        return print("Your argument has to be an array")
    ret = array.copy()
    ret[..., 0] = 0
    ret[..., 1] = 0
    plt.imshow(ret)
    plt.show()
    return ret


def ft_grey(array) -> list:
    '''
    Inverts the color of the image received.
    '''
    if not isinstance(array, np.ndarray):
        return print("Your argument has to be an array")
    ret = array.copy()
    ret[:, :, 0] = array[:, :, 1]
    ret[:, :, 1] = array[:, :, 1]
    ret[:, :, 2] = array[:, :, 1]
    plt.imshow(ret)
    plt.show()
    return ret
