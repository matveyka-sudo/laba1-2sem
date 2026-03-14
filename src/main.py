from src.sources import Source
from src.sources1 import Source1
from src.sources2 import Source2
from src.proc import check


def main() -> None:
    '''Главная функция, точка входа в программу'''
    sources=[
        Source(),
        Source2(),
        Source1("12.txt")
    ]
    result=check(sources)
    for task in result:
        print(task)

if __name__ == "__main__":
    main()
