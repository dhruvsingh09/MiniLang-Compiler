class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None
    def consume(self, expected_type):
        token = self.peek()
        if token and token.type == expected_type:
            self.position += 1
            return token
        raise Exception(f"Expected {expected_type}, but got {token}")
    def parse_expression(self):
        term = self.parse_term()
        while self.peek() and self.peek().type in ("PLUS", "MINUS"):
            op = self.consume(self.peek().type)
            next_term = self.parse_term()
            term = ("BINARY_OP", op.value, term, next_term)
        return term
    def parse_term(self):
        factor = self.parse_factor()
        while self.peek() and self.peek().type in ("MULTIPLY", "DIVIDE"):
            op = self.consume(self.peek().type)
            next_factor = self.parse_factor()
            factor = ("BINARY_OP", op.value, factor, next_factor)
        return factor
    def parse_factor(self):
        if self.peek().type == "NUMBER":
            return ("NUMBER", self.consume("NUMBER").value)
        elif self.peek().type == "IDENTIFIER":
            return ("IDENTIFIER", self.consume("IDENTIFIER").value)
        elif self.peek().type == "LPAREN":
            self.consume("LPAREN")
            expr = self.parse_expression()
            self.consume("RPAREN")
            return expr
        else:
            raise Exception("Invalid factor")
    def parse_statement(self):
        if self.peek().type == "IDENTIFIER":
            identifier = self.consume("IDENTIFIER").value
            self.consume("ASSIGN")
            expression = self.parse_expression()
            self.consume("SEMICOLON")
            return ("ASSIGNMENT", identifier, expression)
        elif self.peek().type == "PRINT":
            self.consume("PRINT")
            self.consume("LPAREN")
            expression = self.parse_expression()
            self.consume("RPAREN")
            self.consume("SEMICOLON")
            return ("PRINT", expression)
        else:
            return self.parse_expression()
    def parse(self):
        statements = []
        while self.peek():
            statements.append(self.parse_statement())
        return statements