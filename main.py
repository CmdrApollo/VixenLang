import os, sys
from src.lexer import Lexer
from src.parser import Parser, pretty_print
from src.resolver import *
from src.interpreter import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            lexer = Lexer(open(sys.argv[1]).read())
            parser = Parser(lexer.lex())

            pretty_print(parser.parse())
        else:
            print("error: invalid file input")
    else:
        print("error: expected file input")