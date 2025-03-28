keywords = {"¬"}

def parse_line(line):
    # Remove comments and strip whitespace
    line = line.split("//")[0].strip()
    
    # Splitting the line into tokens
    current_token = ""
    tokens = []
    for char in line:
        if char in keywords:
            if current_token:
                tokens.append(current_token.strip())
                current_token = ""
            tokens.append(char)
        elif char.isspace():
            if current_token:
                tokens.append(current_token.strip())
                current_token = ""
        else:
            current_token += char
    if current_token:
        tokens.append(current_token.strip())

    return tokens