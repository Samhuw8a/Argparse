from argparser.flags import Option, Vars, Flag
from argparser.filename import filename

class Group():
    def __init__(self,name:str,description:str)->None:
        self.group_flags:list =[]
        self.name = name
        self.description = description

    def add_flag(self,fl:Flag)->None:
        self.group_flags.append(fl)

    def __str__(self)->str:
        desc = f"{self.name}:\n"
        for f in self.group_flags:
            if isinstance(f,Option):
                desc +=f"\t{f.name}: {list(i for i in f.str_reps)}\n"
            elif isinstance(f,Vars):
                desc+=f"\t{f.name}: {list(i for i in f.str_reps)} {*f.types_str(),}\n"
        return desc


def main()->None:
    g = Group("Test_gruppe","eine Test_gruppe")
    g.add_flag(Vars("name", "doc_str",(int,filename),"t"))
    g.add_flag(Option("name", "doc_str","g"))
    print(g)

if __name__ == "__main__":
    main()
