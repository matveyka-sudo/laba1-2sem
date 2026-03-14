from src.models import Tasks
from typing import Iterable

class Source2:
    def generator(self)->Iterable[Tasks]:
        '''метод генерирующий задачи'''
        return [
            Tasks(id=1,payload='1'),
            Tasks(id=2,payload='2'),
            Tasks(id=3,payload='3')
        ]
