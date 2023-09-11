from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def ft_zoom(img: list, origin: list, height: int, width: int) -> list:
    '''
    Rezise an image from a point x, y with a height and width define
    in arguments, then convert the image in grayscale
    '''
    if (not isinstance(img, np.ndarray) or not isinstance(origin, tuple)
            or not len(img)):
        return print("Can't zoom with img or origin argument NULL")
    if not isinstance(height, int) or not isinstance(width, int):
        return print("Height and width arguments have to be integer lower"
                     "than", len(img))
    zoom = img[origin[1]:width + origin[1], origin[0]:height + origin[0]]
    to_gray = np.mean(zoom, axis=2).astype(np.int64)
    to_gray = to_gray.reshape(height, width, 1)
    return to_gray


def ft_rotate(img: list) -> list:
    '''
    Apply a rotation to img.
    '''
    if not isinstance(img, np.ndarray):
        return print("Can't rotate with img argument NULL")
    dim = len(img)
    rotate = [[img[x, y] for x in range(dim)] for y in range(dim)]
    rotate = np.array(rotate)
    rotate = rotate.reshape(dim, dim)
    return rotate


def main():
    '''
    Load in grayscale, print size information and rezise animal.jpeg from a
    point x, y with a height and width then rotate it to 90.
    Finally display the new animal.jpeg.
    '''
    try:
        original = ft_load('animal.jpeg')
        if original is not None:
            resize = ft_zoom(original, (400, 100), 400, 400)
            if resize is not None:
                print("The shape of image is:", np.shape(resize))
                print(resize)
                rotate = ft_rotate(resize)
                if rotate is not None:
                    print("New shape after Transpose:", np.shape(rotate))
                    print(rotate)
                    plt.imshow(rotate, cmap="gray")
                    plt.show()
    except Exception as err:
        print('An error occured', err)


if __name__ == "__main__":
    main()
