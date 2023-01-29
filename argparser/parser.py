from enum import Enum, auto
import sys


class Token(Enum):
    single_str_option = auto()
    multiple_str_option = auto()
    argument = auto()


class Parser:
    def __init__(self, argv: list = sys.argv) -> None:
        self.argv = argv

    def tokenize(self) -> list:
        raise NotImplementedError

    def parse(self) -> dict:
        raise NotImplementedError


def main() -> None:
    pass


if __name__ == "__main__":
    main()
