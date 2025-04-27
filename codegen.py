
class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}
        self.instructions = []
    def generate_expression(self, expr):
        if expr[0] == "NUMBER":
            self.instructions.append(("PUSH", expr[1]))
        elif expr[0] == "IDENTIFIER":
            self.instructions.append(("LOAD", expr[1]))
        elif expr[0] == "BINARY_OP":
            self.generate_expression(expr[2])
            self.generate_expression(expr[3])
            if expr[1] == "+":
                self.instructions.append(("ADD",))
            elif expr[1] == "-":
                self.instructions.append(("SUB",))
            elif expr[1] == "*":
                self.instructions.append(("MUL",))
            elif expr[1] == "/":
                self.instructions.append(("DIV",))
    def generate_statement(self, statement):
        if statement[0] == "ASSIGNMENT":
            self.generate_expression(statement[2])
            self.instructions.append(("STORE", statement[1]))
        elif statement[0] == "PRINT":
            self.generate_expression(statement[1])
            self.instructions.append(("PRINT",))
        else:
            self.generate_expression(statement)
    def generate(self):
        for statement in self.ast:
            self.generate_statement(statement)
        return self.instructions