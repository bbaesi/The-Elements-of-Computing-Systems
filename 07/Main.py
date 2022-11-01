import sys
import Parser
import CodeWriter

def main():
    # 객체 선언 
    parser = Parser.Parser(sys.argv[1])
    write = CodeWriter.CodeWriter(sys.argv[1])

    # hack 파일
    while parser.hasMoreCommands():
        parser.advance()
        # 메모리 접근 명령 처리
        if parser.commandType() == "C_PUSH" or parser.commandType() == "C_POP" :
            write.WritePushPop(parser.commandType(),parser.arg1(),parser.arg2())
        # 산술 명령 처리   
        elif parser.commandType() == "C_ARITHMETIC" :
            write.writerArithmetic(parser.arg1())

    #파일 닫기    
    write.close()

if __name__ == "__main__":
    main()