import sys
import Parser
import CodeWriter

def main():
    # 객체 선언 
    first_parser = Parser.Parser(sys.argv[1])
    second_parser = Parser.Parser(sys.argv[1])
    write = CodeWriter.CodeWriter(sys.argv[1])

    line = -1
    LABEL = { }

    # label 시점 계산
    while first_parser.hasMoreCommands():
        first_parser.advance()
        command = first_parser.arg1()
        # 메모리 접근 명령 계산
        if first_parser.commandType() == "C_PUSH" :
            if (command in "constant") or (command in "temp") or (command in "pointer") or (command in "static") :  
                line += 7    
            else :
                line += 10    
            
        elif first_parser.commandType() == "C_POP" :
            if (command in "constant") or (command in "temp") or (command in "pointer") or (command in "static") :  
                line += 7    
            else :
                line += 14                                  
        # 산술 명령 계산   
        elif first_parser.commandType() == "C_ARITHMETIC" :
            if (command in "eq") or (command in "gt") or (command in "lt"):  
                line += 16
            elif (command in "not") or (command in "neg"):  
                line += 5                     
            else :
                line += 8           
        # 라벨 명령 처리
        elif first_parser.commandType() == "C_LABEL" :
            LABEL[first_parser.arg1()] = line + 1
        # 분기 명령 계산
        elif first_parser.commandType() == "C_GOTO" :
            line += 2
        # 조건 분기 명령 계산
        elif first_parser.commandType() == "C_IF" :
            line += 14                   
        # 함수 호출 명령 계산
        # elif first_parser.commandType() == "C_CALL" :
        #     write.writeCall(first_parser.arg1())
        # 호출 반환 명령 처리
        elif first_parser.commandType() == "C_RETURN" :
            line += 50
        # 함수 코드 시작                
        elif first_parser.commandType() == "C_FUNCTION" :
            line += (8 + 2 * int(first_parser.arg2()))
        # print(write.line)
        print(line)
    write.setLabel(LABEL)


    # hack 파일
    while second_parser.hasMoreCommands():
        second_parser.advance()
        # 메모리 접근 명령 처리
        if second_parser.commandType() == "C_PUSH" or second_parser.commandType() == "C_POP" :
            write.writePushPop(second_parser.commandType(),second_parser.arg1(),second_parser.arg2())
        # 산술 명령 처리   
        elif second_parser.commandType() == "C_ARITHMETIC" :
            write.writerArithmetic(second_parser.arg1())
        # 라벨 명령 처리
        elif second_parser.commandType() == "C_LABEL" :
            write.writelabel(second_parser.arg1())
        # 분기 명령 처리
        elif second_parser.commandType() == "C_GOTO" :
            write.writeGoto(second_parser.arg1())
        # 조건 분기 명령 처리
        elif second_parser.commandType() == "C_IF" :
            write.writeIf(second_parser.arg1())
        # 함수 호출 명령 처리
        # elif second_parser.commandType() == "C_CALL" :
        #     write.writeCall(second_parser.arg1())
        # 호출 반환 명령 처리
        elif second_parser.commandType() == "C_RETURN" :
            write.writeReturn()      
        # 함수 코드 시작                
        elif second_parser.commandType() == "C_FUNCTION" :
            write.writeFunction(second_parser.arg1(),second_parser.arg2())                                                                  

    # 파일 닫기    
    write.close()

if __name__ == "__main__":
    main()