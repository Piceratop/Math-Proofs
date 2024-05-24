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
    print(code_lines)
    for code in code_lines:
        tokens = code.strip().split(maxsplit=-1)
        if tokens[0] == "let":
            if len(tokens) == 2:
                validate_nonkeyword(tokens[1])
                math_variables[tokens[1]] = {
                    "type": "any",
                    "value": None
                }
            elif len(token) < 2:
                print(f"Syntax error:' {tokens[0]} ' was expected, but got ' {tokens[1]} ' instead.")
                exit(1)
            else:
                validate_nonkeyword(tokens[1])
                validate_required_keyword(tokens[2], "=")
                bracket_stack = []
                for tok in tokens[3:]:
                    if tok == "{":
                        bracket_stack.append(tok)
                    elif tok == "}":
                        while True:
                            curr_v = set()
                            if len(bracket_stack) == 0:
                                print("Syntax error: Missing ' } '")
                                exit(1)
                            if bracket_stack[-1] == "{":
                                bracket_stack.pop()
                                bracket_stack
                                break
                            curr_v.add(bracket_stack.pop())

                        

# print(math_variables)