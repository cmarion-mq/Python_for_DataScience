import sys


def charracters_details(str: str):
    '''
    Sum and print the different types of charaters in str
    '''
    print("The text contains", len(str), "characters:")
    print(sum(1 for c in str if c.isupper()), "upper letters")
    print(sum(1 for c in str if c.islower()), "lower letters")
    print(sum(1 for c in str if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"),
          "punctuation marks")
    print(sum(1 for c in str if c.isspace()), "spaces")
    print(sum(1 for c in str if c.isdigit()), "digits")


def main():
    '''
    Main funcion.
    Sum and print the different types of charaters in a str defined in argument
    or prompted.
    '''
    try:
        args = sys.argv
        if len(args) > 2:
            print('AssertionError: more than one argument is provided')
        elif len(args) == 2:
            charracters_details(args[1])
        else:
            str = input("What is the text to count?\n")
            charracters_details(str + ' ')
    except Exception as err:
        print('An error occured', err)


if __name__ == "__main__":
    main()
