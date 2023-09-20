from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King Class'''
    def get_eyes(self) -> str:
        '''King Class eyes getter'''
        return self.eyes

    def get_hairs(self) -> str:
        '''King Class hairs getter'''
        return self.hairs

    def set_eyes(self, eyes: str):
        '''King Class eyes setter. Take one string argument'''
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        '''King Class hairs setter. Take one string argument'''
        self.hairs = hairs
