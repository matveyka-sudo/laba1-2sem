import logging
from src.models import Tasks
from typing import Iterable
from src.logg import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class Source1:
    def __init__(self,path:str):
        self.path=path

    def generator(self)->Iterable[Tasks]:
        '''метод генерирующий задачи'''
        with open(self.path,"r") as f:
            for line in f.readlines():
                privet=line.split(" ")
                tasks=Tasks(id=int(privet[0]),payload=privet[1])
                logger.info("задача сгенерирована")
                yield tasks
