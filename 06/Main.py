import sys
import Parser


def main():
    parser = Parser.Parser(sys.argv[1])
    command = parser.instructions[parser.line]
    # Code = Code.Code()
    while parser.hasMoreCommands():
        parser.advance()
        if command != "" :
            if parser.commandType != 0 : 
                print("test")

if __name__ == "__main__":
    main()