import sys

NESTED_MORSE = {
    ' ': '/',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}


def main():
    '''
    Take a string as an argument and encodes it into Morse Code.
        •The program supports space and alphanumeric characters
        •An alphanumeric character is represented by dots . and dashes -
        •Complete morse characters are separated by a single space
        •A space character is represented by a slash /
    '''
    try:
        args = sys.argv
        if len(args) != 2:
            return print('AssertionError: the arguments are bad')

        str = args[1].upper()
        if len([c for c in str if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
                or not c.isprintable() or c not in NESTED_MORSE]):
            return print('AssertionError: the arguments are bad')
        trad = [NESTED_MORSE[c] for c in str]
        return print(" ".join(trad))
    except Exception as err:
        print('An error occured', err)


if __name__ == "__main__":
    main()
