import re


class filename(str):
    def __init__(self, string: str) -> None:
        super().__init__()
        p = re.compile("^(\/?(\w+|\.{1,2}))+(\.\w+)?$")
        if not re.fullmatch(p, self):
            raise ValueError("Incorrect filename format")
