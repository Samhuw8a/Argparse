class FlagException(Exception): pass
class FlagFormatError(FlagException): pass

class OptionException(FlagException): pass


class VarException(FlagException): pass

class VarArgumentException(VarException): pass

class InvalidArgType(VarArgumentException): pass

class VarArgumentCountException(VarArgumentException): pass

class TooManyVarArguments(VarArgumentCountException): pass
class       NoVarArgument(VarArgumentCountException): pass
