from ast import AST

class Num(AST):
    def __init__(self, token, value):
        self.token = token
        self.value = value