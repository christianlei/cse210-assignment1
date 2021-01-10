class Parser:
    def __init__(self, parsed_string):
        self.ast = None
        self.parsed_list = parsed_string.split(' ')

    def string_to_AST(self):
        ast = None
        while not self.parsed_list:
            item = self.parsed_list.pop(0)
            if item == '+':
                bin_op = BinOp(ast, '+', Num(self.parsed_list.pop(0)))
                prev_item = bin_op
            elif item == '*':
                bin_op = BinOp(ast, '+', Num(self.parsed_list.pop(0)))
                prev_item = bin_op
            else:
                num = Num('int' ,item)
                prev_item = num
                
        self.ast = ast