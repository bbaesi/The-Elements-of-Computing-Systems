import sys
import Parser

def main():
    # 객체 선언 
    parser = Parser.Parser(sys.argv[1])

    # 파일 열기
    output = sys.argv[1].split('.vm')[0] + '.asm'
    hack = open(output, "a")

    # hack 파일
    while parser.hasMoreCommands():
        parser.advance()

    #파일 닫기    
    hack.close()

if __name__ == "__main__":
    main()