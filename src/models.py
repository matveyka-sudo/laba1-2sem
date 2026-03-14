from dataclasses import dataclass
from typing import Any

@dataclass
class Tasks:
    '''Класс содержащий необходимые поля(имитирующий задачу)'''
    id:int
    payload:Any
