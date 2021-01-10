import argparse
from parser import Parser
from interpreter import Interpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('exp_str', type=str)
    args = parser.parse_args()
    string_parser = Parser(args.exp_str)
    interpreter = Interpreter()

    string_parser.string_to_AST()
    result = interpreter.eval(string_parser.ast)
    print(result)
    return result

if __name__ == '__main__':
    main()