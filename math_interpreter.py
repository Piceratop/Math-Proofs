from math_error import *

with open("test.mthc", "r") as f:
    code = f.read().strip().split()
    # The "set" command
    if code[0] == "set":
        code = code[1:]
        if len(code) == 0:
            raise CommandLengthException('set', 1)
    else:
        pass