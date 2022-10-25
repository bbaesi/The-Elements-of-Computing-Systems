import sys
import Parser
import CodeWriter

def main():
    # 객체 선언 
    parser = Parser.Parser(sys.argv[1])
    write = CodeWriter.CodeWriter(sys.argv[1])

    # parser = Parser.Parser("./test/gt.vm")
    # write = CodeWriter.CodeWriter("./test/gt.vm")    

    # hack 파일
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == "C_PUSH" or parser.commandType() == "C_POP" :
            write.WritePushPop(parser.commandType(),parser.arg1(),parser.arg2())
        if parser.commandType() == "C_ARITHMETIC" :
            write.writerArithmetic(parser.arg1())

    #파일 닫기    
    write.close()

if __name__ == "__main__":
    main()