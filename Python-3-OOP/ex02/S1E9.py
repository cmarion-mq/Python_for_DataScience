from abc import ABC, abstractmethod


class Character(ABC):
    '''Your docstring for Class'''
    def __init__(self, name: str, is_alive=True):
        '''Your docstring for Constructor'''
        try:
            self.first_name = name
            self.is_alive = is_alive
        except Exception as err:
            print(err)

    @abstractmethod
    def die(self):
        '''Your docstring for Method'''
        pass


class Stark(Character):
    '''Your docstring for Class'''
    def __init__(self, name: str, is_alive=True):
        '''Your docstring for Constructor'''
        try:
            Character.__init__(self, name, is_alive)
        except Exception as err:
            print(err)

    def die(self):
        '''Your docstring for Method'''
        try:
            self.is_alive = not self.is_alive
        except Exception as err:
            print(err)
