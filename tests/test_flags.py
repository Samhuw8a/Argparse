from argparser.flags import *

def setup_Flag()->Flag:
    return Flag("name","doc_str","h","help")

def setup_Vars()->Vars:
    return Vars("name","doc_str",(int,str,float),"h","help")

def test_Flag_docstr()->None:
    f = setup_Flag()
    assert str(f) == "doc_str"

def test_Flag_str_reps()->None:
    f = setup_Flag()
    assert len(f) == 2

def test_Vars_arg_count()->None:
    v = setup_Vars()
    assert v.arg_count == len(v.arg_types)
