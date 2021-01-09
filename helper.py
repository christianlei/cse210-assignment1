class Helper:
    def __init__(self, parsed_string):
        self.ast = AST()
        self.parsed_list = parsed_string.split(' ')

    def string_to_AST(self):
        for item in parsed_list:
            if item == '+':
                add_token = Token(ADD, item)
            elif item == '*':
                mul_token = Token(MUL, item)
            else:
                num_token = Token(INTEGER, item)

    def eval(self, intExp=None, sumExp=None, mulExp=None):
        if intExp is not None:
            return intExp
        if sumExp is not None:
            return eval(sumExp[0]) + eval(sumExp[1])
        if mulExp is not None:
            return eval(mulExp[0]) * eval(mulExp[1])