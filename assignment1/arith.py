from parser import Parser
from interpreter import Interpreter


def main():
    val = input() 
    string_parser = Parser(val)
    interpreter = Interpreter()

    string_parser.string_to_AST()
    result = interpreter.eval(string_parser.ast)
    print(result)
    return result


if __name__ == '__main__':
    main()
