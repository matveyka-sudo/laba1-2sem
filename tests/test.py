import pytest
from src.models import Tasks
from src.proc import check
from src.sources import Source
from src.sources1 import Source1
from src.sources2 import Source2



class Test:
    def test(self):
        assert check([Source()])==[Tasks(id=0, payload='payload 0'),
 Tasks(id=1, payload='payload 1'),
 Tasks(id=2, payload='payload 2'),
 Tasks(id=3, payload='payload 3'),
 Tasks(id=4, payload='payload 4'),
 Tasks(id=5, payload='payload 5'),
 Tasks(id=6, payload='payload 6'),
 Tasks(id=7, payload='payload 7'),
 Tasks(id=8, payload='payload 8'),
 Tasks(id=9, payload='payload 9')]
        assert check([Source2()])==[Tasks(id=1, payload='1'), Tasks(id=2, payload='2'), Tasks(id=3, payload='3')]
        assert check(['123']) == []
        assert check([Source(),Source2()])==[Tasks(id=0, payload='payload 0'),
 Tasks(id=1, payload='payload 1'),
 Tasks(id=2, payload='payload 2'),
 Tasks(id=3, payload='payload 3'),
 Tasks(id=4, payload='payload 4'),
 Tasks(id=5, payload='payload 5'),
 Tasks(id=6, payload='payload 6'),
 Tasks(id=7, payload='payload 7'),
 Tasks(id=8, payload='payload 8'),
 Tasks(id=9, payload='payload 9'),
 Tasks(id=1, payload='1'),
 Tasks(id=2, payload='2'),
 Tasks(id=3, payload='3')]
        assert check([Source])==[]
