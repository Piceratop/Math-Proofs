class CommandLengthException(Exception):
    def __init__(self, command, length):
        self.command = command
        self.length = length

    def __str__(self):
        return f"Command {self.command} has length {self.length}"