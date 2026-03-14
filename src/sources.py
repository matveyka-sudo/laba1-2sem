import logging
from src.models import Tasks
from typing import Iterable
from src.logg import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

class Source:
    def generator(self)->Iterable[Tasks]:
        '''метод генерирующий задачи'''
        for i in range(0,10):
            tasks=Tasks(id=i,payload=f"payload {i}")
            logger.info("задача сгенерирована")
            yield tasks
