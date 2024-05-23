math_variables = dict()

def check_command_length(command, min_length, max_length, given):
    if given < min_length or given > max_length:
        print(f"Invalid number of arguments for {command}, expected between {min_length} and {max_length}, got {given}")
        exit(1)

def check_unknown_variable(name):
    if name not in math_variables:
        print(f"'{name}' is not defined")
        exit(1)

def unknown_command(command):
    print(f"Unknown command: {command}")
    exit(1)

with open("test.mthc", "r") as f:
    for code_line in f.readlines():
        code = code_line.strip().split(maxsplit=-1)
        # "assign" command
        if code[0] == "assign":
            code = code[1:]
            check_command_length("assign", 2, float('inf'), len(code))
            var_name = code[0]
            check_unknown_variable(var_name)
            math_variables[var_name]["value"] = set()
            for value in code[1:]:
                math_variables[var_name]["value"].add(value)

        # "set" command
        elif code[0] == "set":
            code = code[1:]
            check_command_length("set", 1, 1, len(code))
            math_variables[code[0]] = {
                "value": set(),
                "type": "set"
            }
        else:
            unknown_command(code[0])

print(math_variables)