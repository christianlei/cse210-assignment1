from binop import BinOp
from num import Num


class Interpreter:

    def eval(self, ast):
        if isinstance(ast, BinOp):
            if ast.op == '+':
                return self.eval(ast.left) + self.eval(ast.right)
            if ast.op == '*':
                return self.eval(ast.left) * self.eval(ast.right)
            if ast.op == '-':
                return self.eval(ast.left) - self.eval(ast.right)

        if isinstance(ast, Num):
            return int(ast.value)
