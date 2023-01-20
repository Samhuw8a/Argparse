from abc import ABC

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
    def __init__(self,name:str, doc_str:str, arg_count:int, arg_types:tuple, *str_reps)->None:
        super().__init__(name, doc_str, *str_reps)
        self.arg_count = arg_count
        self.arg_types = arg_types
        #TODO excetions
        assert len(arg_types)==arg_count

def main()->None:
    v = Option("name","doc_str","tsep","h")
    print(len(v))

if __name__ == "__main__":
    main()
