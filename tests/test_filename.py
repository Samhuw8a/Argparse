from argparser.filename import *
import pytest

def test_filename_checking()->None:
    fn = filename("/asf/test.py")
    with pytest.raises(ValueError):
        fn = filename("/asdf/afsd/")
