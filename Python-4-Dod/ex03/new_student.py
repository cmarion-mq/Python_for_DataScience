import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generate a random str id and return it'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Class Student, need as arguments a name and nickname.
    Automatic generation of active, login and id attributes.'''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: int = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()
