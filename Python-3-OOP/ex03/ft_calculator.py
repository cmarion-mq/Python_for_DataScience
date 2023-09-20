class calculator:
    '''Calculator class'''
    def __init__(self, vector: list):
        '''Class Calculator constructeur. Take a lits in argument'''
        try:
            self.vector = vector
        except Exception as err:
            print(err)

    def __add__(self, object) -> None:
        '''Class Calculator addition method. Take a scalar in argument'''
        try:
            self.vector = [val + object for val in self.vector]
            return print(self.vector)
        except Exception as err:
            print(err)

    def __mul__(self, object) -> None:
        '''Class Calculator multiplication method. Take a scalar in argument'''
        try:
            self.vector = [val * object for val in self.vector]
            return print(self.vector)
        except Exception as err:
            print(err)

    def __sub__(self, object) -> None:
        '''Class Calculator subtraction method. Take a scalar in argument'''
        try:
            self.vector = ([val - object for val in self.vector])
            return print(self.vector)
        except Exception as err:
            print(err)

    def __truediv__(self, object) -> None:
        '''Class Calculator true division method. Take a scalar in argument'''
        try:
            if object == 0:
                return print("AssertionError: division by 0 is impossible")
            self.vector = ([val / object for val in self.vector])
            print(self.vector)
        except Exception as err:
            print(err)
