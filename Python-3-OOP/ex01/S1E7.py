from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, name: str, is_alive=True):
        '''Your docstring for Constructor'''
        try:
            Character.__init__(self, name, is_alive)
            self.family_name = "Baratheon"
            self.eyes = "brown"
            self.hairs = "dark"
        except Exception as err:
            print(err)

    def die(self):
        '''Your docstring for Method'''
        try:
            self.is_alive = not self.is_alive
        except Exception as err:
            print(err)

    def __str__(self) -> str:
        '''Your docstring for __str__ informations'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Your docstring for __repr__ informations'''
        return self.__str__()


class Lannister(Character):
    '''Representing the Lannister family.'''
    def __init__(self, name: str, is_alive=True):
        '''Your docstring for Constructor'''
        try:
            Character.__init__(self, name, is_alive)
            self.family_name = "Lannister"
            self.eyes = "blue"
            self.hairs = "light"
        except Exception as err:
            print(err)

    def die(self):
        '''Your docstring for Method'''
        try:
            self.is_alive = not self.is_alive
        except Exception as err:
            print(err)

    def __str__(self) -> str:
        '''Your docstring for for __str__ informations'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        '''Your docstring for __repr__ informations'''
        return self.__str__()

    @classmethod
    def create_lannister(cls, name: str, is_alive=True):
        '''Your docstring for Create ClassMethod'''
        try:
            return cls(name, is_alive)
        except Exception as err:
            print(err)
