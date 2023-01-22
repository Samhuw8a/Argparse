from abc import ABC
from filename import filename

class Flag(ABC):
    def __init__(self,name:str, doc_str:str, *str_rep)->None:
        self.name = name
        self.doc_str = doc_str
        self.str_reps = str_rep

    def __str__(self)->str:
        return self.doc_str

    def __len__(self)->int:
        return len(self.str_reps)

class Option(Flag):
    pass

class Vars(Flag):
    def __init__(self,name:str, doc_str:str, arg_types:tuple, *str_reps)->None:
        super().__init__(name, doc_str, *str_reps)
        self.arg_types = arg_types
        self.arg_count = len(arg_types)

    def types_str(self)->tuple:
        tps=[]
        for i in self.arg_types:
            if i == int: tps.append("int")
            elif i == str: tps.append("str")
            elif i == float: tps.append("float")
            elif i == filename: tps.append("filename")
        return tuple(tps)

def main()->None:
    o = Option("name","doc_str","tsep","h")
    v = Vars("name","doc_str",(filename,int),"a")
    print(o)
    print(v)

if __name__ == "__main__":
    main()
