import sys
import Parser
import Code


def main():
    # 클래스 선언
    parser = Parser.Parser(sys.argv[1])
    code = Code.Code()

    # hack 파일 생성 준비
    output = sys.argv[1].split('.asm')[0] + '.hack'
    hack = open(output, "a")

    # hack 파일
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == "C_COMMAND" :
            a = code.comp(parser.comp())
            b = code.dest(parser.dest()) 
            c = code.jump(parser.jump())
            COMMAND= "111"+a+b+c
        else:
            A_COMMAND = bin(int(parser.symbol()))[2:]
            COMMAND = A_COMMAND.zfill(16)
        hack.writelines(COMMAND+"\n")

    hack.close()

if __name__ == "__main__":
    main()