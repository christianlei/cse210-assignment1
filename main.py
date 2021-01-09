import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('expression string', type=str)
    args = parser.parse_args()
    string_parser = Parser()

if __name__ == '__main__':
    main()