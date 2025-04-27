import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"
class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
    def get_next_token(self):
        if self.position >= len(self.source):
            return None
        while self.position < len(self.source) and self.source[self.position].isspace():
            self.position += 1
        if self.position >= len(self.source):
            return None
        if self.source[self.position:self.position + 2] == "//":
            while self.position < len(self.source) and self.source[self.position] != '\n':
                self.position += 1
            return self.get_next_token()
        if self.position >= len(self.source):
            return None
        if self.source[self.position].isdigit():
            number = ""
            while self.position < len(self.source) and self.source[self.position].isdigit():
                number += self.source[self.position]
                self.position += 1
            return Token("NUMBER", int(number))
        if self.source[self.position].isalpha():
            identifier = ""
            while self.position < len(self.source) and self.source[self.position].isalnum():
                identifier += self.source[self.position]
                self.position += 1
            if identifier == "print":
                return Token("PRINT", identifier)
            return Token("IDENTIFIER", identifier)
        if self.source[self.position] == '+':
            self.position += 1
            return Token("PLUS", "+")
        elif self.source[self.position] == '-':
            self.position += 1
            return Token("MINUS", "-")
        elif self.source[self.position] == '*':
            self.position += 1
            return Token("MULTIPLY", "*")
        elif self.source[self.position] == '/':
            self.position += 1
            return Token("DIVIDE", "/")
        elif self.source[self.position] == '=':
            self.position += 1
            return Token("ASSIGN", "=")
        elif self.source[self.position] == ';':
            self.position += 1
            return Token("SEMICOLON", ";")
        elif self.source[self.position] == '(':
            self.position += 1
            return Token("LPAREN", "(")
        elif self.source[self.position] == ')':
            self.position += 1
            return Token("RPAREN", ")")
        raise Exception(f"Invalid character: {self.source[self.position]}")