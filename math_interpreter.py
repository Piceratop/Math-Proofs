math_variables = dict()
keywords = {"=", "let", "{", "}"}

def validate_minimum(tokens, keyword, required):
    if len(tokens) < required:
        print(f"Syntax error: ' {keyword} ' requires at least {required - 1} arguments.")
        exit(1)

def validate_nonkeyword(token):
    if token in keywords:
        print(f"Syntax error: ' {token} ' is a keyword.")
        exit(1)

def validate_required_keyword(token, keyword):
    if token != keyword:
        print(f"Syntax error: ' {keyword} ' was expected, but got ' {token} ' instead.")
        exit(1)


with open("test.mthc", "r") as f:
    code_lines = f.readlines()
    for code in code_lines:
        tokens = code.strip().split(maxsplit=-1)
        if tokens[0] == "let":
            if len(tokens) == 2:
                validate_nonkeyword(tokens[1])
                math_variables[tokens[1]] = {
                    "type": "any",
                    "value": None
                }
            else:
                validate_nonkeyword(tokens[1])
                validate_required_keyword(tokens[2], "=")
                bracket_stack = []
                curr_v = set()
                for tok in tokens[3:]:
                    if tok == "}":
                        while True:
                            if len(bracket_stack) == 0:
                                print("Syntax error: Missing ' { '")
                                exit(1)
                            if bracket_stack[-1] == "{":
                                bracket_stack.pop()
                                bracket_stack.append(curr_v)
                                curr_v = set()
                                break
                            curr_v.add(bracket_stack.pop())
                    else:
                        bracket_stack.append(tok)
                if (len(bracket_stack) != 1):
                    print("Syntax error: Too many variable assignments.")
                    exit(1)
                math_variables[tokens[1]] = {
                    "type": "set",
                    "value": bracket_stack[0]
                }

print(math_variables)