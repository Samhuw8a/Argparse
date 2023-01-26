from typing import Any
from argparser.flags import Option, Vars, Flag
from argparser.filename import filename

class Group():
    def __init__(self,name:str,description:str)->None:
        self._group_flags:dict ={}
        self._group_values:dict={}
        self.name = name
        self.description = description

    def list_flags(self)->list:
        return list(self._group_flags.keys())

    def add_flag(self,fl:Flag)->None:
        self._group_flags[fl.name] = fl
        #TODO type user_spec default values
        self._group_values[fl.name] = None
        print(fl)

    def __getitem__(self,name:str)->Flag:
        return self._group_flags[name]

    def set_value_to_flag(self,flag:Flag, *value:Any)->None:
        self._group_values[flag.name] = list(value)

    def __str__(self)->str:
        desc = f"{self.name}:\n"
        for f in self._group_flags.values():
            if isinstance(f,Option):
                desc +=f"\t{f.name}: {list(i for i in f.str_reps)}\n"
            elif isinstance(f,Vars):
                desc+=f"\t{f.name}: {list(i for i in f.str_reps)} {*f.types_str(),}\n"
        return desc


def main()->None:
    g = Group("Test_gruppe","eine Test_gruppe")
    g.add_flag(Vars("asfs", "doc_str",(int,filename),"t"))
    g.set_value_to_flag(g["asfs"], 1,"asdf")
    print(g._group_values)
    print(g)

if __name__ == "__main__":
    main()
