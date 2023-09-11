import cv2 as cv


def ft_load(path: str) -> list:
    '''
    Load an image, prints its format, and its pixels content in grayscale
    format.
    '''
    try:
        im = cv.imread(path)
        if im is None:
            return print("Could not read the image, check the path.",
                         "Your image should be a JPG or JPEG format")
        img = cv.cvtColor(im, cv.COLOR_BGR2RGB)   # BGR -> RGB
        if img is None:
            return print("Could not convert the image.")
        return img
    except Exception as err:
        print('An error occured', err)
