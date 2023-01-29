from argparser.exceptions import *
from argparser.groups import *
from argparser.filename import *
from argparser.parser import *
from argparser.flags import *
from argparser.type_checker import *


class Argparser:
    def __init__(self):
        raise NotImplementedError

    def get_flags(self) -> dict:
        raise NotImplementedError
