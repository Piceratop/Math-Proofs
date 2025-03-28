from math_parser import parse_line
# keywords = {"¬"}

class MathError(Exception):
    def __init__(self, message):
        super().__init__(message)

with open("test.mthc", "r", encoding="utf-8") as f:
    for line in f:
        tokenized_line = parse_line(line)
        if not tokenized_line:
            continue
        print(tokenized_line)
