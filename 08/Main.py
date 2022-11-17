import sys
import Parser
import CodeWriter
import os

def main():
    # 디렉토리 열기
    path = sys.argv[1]
    file_list = os.listdir(path)
    file_list_vm = [file for file in file_list if file.endswith(".vm")]
    if "Sys.vm" in file_list_vm:
        file_list_vm.remove("Sys.vm")
        file_list_vm.insert(0, 'Sys.vm')
    print ("========== compile set ===========")
    print ("    - file_list: {} ".format(file_list_vm))
    
    line = -1
    
    for i in file_list_vm :
        file = sys.argv[1]+"/"+i
        print ("========= compile start ==========".format(i))
        print ("    - {} is ready ".format(i))

        first_parser = Parser.Parser(file)
        second_parser = Parser.Parser(file)
        write = CodeWriter.CodeWriter(file)

        LABEL = { }
        write.line = line        


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
                    line += 19
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
            elif first_parser.commandType() == "C_CALL" :
                line += 46                   
            # 호출 반환 명령 처리
            elif first_parser.commandType() == "C_RETURN" :
                line += 50
            # 함수 코드 시작                
            elif first_parser.commandType() == "C_FUNCTION" :
                line += (8 + 2 * int(first_parser.arg2()))
            # print(write.line)
        write.setLabel(LABEL)
        print("    - label : " +str(LABEL))


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
            elif second_parser.commandType() == "C_CALL" :
                write.writeCall(second_parser.arg1(),second_parser.arg2())     
            # 호출 반환 명령 처리
            elif second_parser.commandType() == "C_RETURN" :
                write.writeReturn()      
            # 함수 코드 시작                
            elif second_parser.commandType() == "C_FUNCTION" :
                write.writeFunction(second_parser.arg1(),second_parser.arg2())                                                                  
        # 파일 닫기    
        write.close()
    print ("======== compile success =========")

if __name__ == "__main__":
    main()