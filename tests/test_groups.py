from argparser.groups import Multilevel_namespace
from typing import Any

import pytest


def test_Multilevel_namespace() -> None:
    n: Any = Multilevel_namespace({"a": "a", "sub": {"b": "b", "c": "c"}, "d": "d"})
    assert n.a == "a"
    assert n.d == "d"
    assert n.sub.b == "b"
    assert n.sub.c == "c"


def test_Multilevel_namespace_false_args() -> None:
    with pytest.raises(AttributeError):
        n = Multilevel_namespace({1: "asdf"})
