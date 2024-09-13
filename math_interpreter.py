variables_dict = {}
ketwords = {":=", "{", "}", "∅"}

def parse_tokens(line):
    tokens_list = []
    current_token = ""
    for ch in line:
        if ch.isspace():
            if current_token:
                tokens_list.append(current_token)
                current_token = ""
        elif ch == "{" or ch == "}":
            if current_token:
                tokens_list.append(current_token)
                current_token = ""
            tokens_list.append(ch)
        else:
            current_token += ch
    if current_token:
        tokens_list.append(current_token)
    return tokens_list

with open("test.mthc", "r") as f:
    for line in f:
        line = parse_tokens(line)
        print(line)
