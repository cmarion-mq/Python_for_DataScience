import sys
from ft_filter import ft_filter


def main():
    '''
    Main funcion.
    Output a list of words from a string (first argument) that have
    a length greater than the integer (second argument).
    String words are separated from each other by space characters.
•	String do not contain any special characters. (Punctuation or invisible)
    '''
    try:
        args = sys.argv
        if len(args) != 3:
            return print('AssertionError: the arguments are bad')

        str = args[1]
        if len([x for x in str if x in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
                or not x.isprintable()]):
            return print('AssertionError: the arguments are bad')
        try:
            n = int(args[2])
        except Exception:
            print('AssertionError: the arguments are bad')
        else:
            return print(ft_filter(lambda word: len(word) > n, str.split()))
    except Exception as err:
        print('An error occured', err)


if __name__ == "__main__":
    main()
