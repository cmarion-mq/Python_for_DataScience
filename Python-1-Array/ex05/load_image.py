import cv2 as cv
import numpy as np


def ft_load(path: str) -> list:
    '''
    Load an image, prints its format, and its pixels content in RGB format.
    '''
    try:
        im = cv.imread(path)
        if im is None:
            return print("Could not read the image, check the path."
                         " Your image should be a JPG or JPEG format")
        img = cv.cvtColor(im, cv.COLOR_BGR2RGB)   # BGR -> RGB
        if img is None:
            return print("Could not convert the image.")
        print("The shape of image is:", np.shape(img))
        print(img)
        return img
    except Exception as err:
        print('An error occured', err)
