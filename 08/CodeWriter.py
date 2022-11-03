class CodeWriter:

    # ** CodeWriter 기록 준비 ** #
    def __init__(self, path):
        self.path = path
        self.file = self.path.split('.vm')[0]
        self.filename = self.file.split('/')[-1]
        self.output_file = open(self.file+ '.asm','w')   
        self.line = -1 
        self.LABEL = { }
        self.functionName = ""

    # ** 산술 명령 어셈블리 코드 기록 ** #
    def writerArithmetic(self, command):   
        # 스택 포인터 재지정
        self.output_file.writelines("@SP\n")
        self.output_file.writelines("AM=M-1\n")  
        self.line += 2               
        # 산술 명령 번역 시작  
        if command == "add" :              
            self.output_file.writelines("D=M\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.output_file.writelines("M=M+D\n")
            self.line += 4          
        elif command == "sub" :            
            self.output_file.writelines("D=M\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.output_file.writelines("M=M-D\n")
            self.line += 4
        elif command == "neg" :   
            self.output_file.writelines("M=-M\n")  
            self.line += 1
        elif command == "eq" : 
            # 조건문 점프 
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@%s\n" % str(self.line + 2 + 4)) 
            self.output_file.writelines("D;JEQ\n")   
            self.output_file.writelines("@%s\n" % str(self.line + 4 + 5)) 
            self.output_file.writelines("D;JNE\n")
            # 같을 경우 
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@%s\n" % str(self.line + 7 + 3)) 
            self.output_file.writelines("0;JMP\n")   
            # 다를 경우 
            self.output_file.writelines("D=0\n")  
            # 결과 반영 
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")
            self.output_file.writelines("M=D\n")  
            self.line += 12
        elif command == "gt" : 
            # 조건문 점프 
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@%s\n" % str(self.line + 2 + 4)) 
            self.output_file.writelines("D;JGT\n")   
            self.output_file.writelines("@%s\n" % str(self.line + 4 + 5)) 
            self.output_file.writelines("D;JLE\n")       
            # 클 경우 
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@%s\n" % str(self.line + 7 + 3)) 
            self.output_file.writelines("0;JMP\n")   
            # 같을 경우 + 작을 경우 
            self.output_file.writelines("D=0\n")
            # 결과 반영 
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")            
            self.output_file.writelines("M=D\n")  
            self.line += 12
        elif command == "lt" : 
            # 조건문 점프 
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@%s\n" % str(self.line + 2 + 4)) 
            self.output_file.writelines("D;JLT\n")   
            self.output_file.writelines("@%s\n" % str(self.line + 4 + 5)) 
            self.output_file.writelines("D;JGE\n")       
            # 클 경우 
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@%s\n" % str(self.line + 7 + 3)) 
            self.output_file.writelines("0;JMP\n")   
            # 같을 경우 + 작을 경우 
            self.output_file.writelines("D=0\n")
            # 결과 반영 
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")            
            self.output_file.writelines("M=D\n")  
            self.line += 12          
        elif command == "and" :         
            self.output_file.writelines("D=M\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.output_file.writelines("M=M&D\n")
            self.line += 4          
        elif command == "or" : 
            self.output_file.writelines("D=M\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")              
            self.output_file.writelines("M=M|D\n") 
            self.line += 4    
        elif command == "not" :        
            self.output_file.writelines("M=!M\n")   
            self.line += 1
        # 스택 포인터 다음 명령어 실행 위치로 조정  
        self.output_file.writelines("@SP\n")
        self.output_file.writelines("AM=M+1\n\n")                            
        self.line += 2                 
      
    # ** command 번역 후 어셈블리 코드 기록 ** #
    # @LCL  
    # A=M+index
    # 위 처럼 진행하면 시뮬레이터에서 오류가 발생한다. 정적변수 하나 만들어 저장 해준다.
    def writePushPop(self, command, segment, index):
        num = int(index) 
        # ** PUSH case **  #        
        if command == "C_PUSH":
            if segment == "constant" :             
                self.output_file.writelines("@%s\n" % str(num))  
                self.output_file.writelines("D=A\n")
                self.line += 2                  
            elif segment == "temp" :
                self.output_file.writelines("@%s\n" % str(num+5))  
                self.output_file.writelines("D=M\n")
                self.line += 2   
            elif segment == "pointer" :
                if num == 0 :
                    self.output_file.writelines("@THIS\n") 
                elif num == 1 :
                    self.output_file.writelines("@THAT\n")   
                self.output_file.writelines("D=M\n")
                self.line += 2  
            elif segment == "static" :
                self.output_file.writelines("@%s.static%s\n" % (self.filename, index))  
                self.output_file.writelines("D=M\n")
                self.line += 2                  
            # 아래 segment는 함수 세팅 값에 따라 초기값이 달라 질 수 있기 때문에 숫자로 하드 코딩 x                                         
            else :     
                self.output_file.writelines("@%s\n" % index)   
                self.output_file.writelines("D=A\n")    
                if segment == "local" :        
                    self.output_file.writelines("@LCL\n")     
                elif segment == "argument" :         
                    self.output_file.writelines("@ARG\n")               
                elif segment == "this" :         
                    self.output_file.writelines("@THIS\n")               
                elif segment == "that" :         
                    self.output_file.writelines("@THAT\n")                              
                self.output_file.writelines("A=D+M\n")    
                self.output_file.writelines("D=M\n")
                self.line += 5 
            # 스택에 저장 후 sp 1 증가    
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")
            self.output_file.writelines("M=D\n")                   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("M=M+1\n\n")
            self.line += 5                 
                                   
        # ** POP case ** #     
        if command == "C_POP":
            # POP 준비        
            if segment == "constant" :             
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("AM=M-1\n")             
                self.output_file.writelines("D=M\n")                   
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("M=D\n") 
                self.output_file.writelines("@SP\n") 
                self.output_file.writelines("A=M\n\n")
                self.line += 7    
            elif segment == "temp" :
                self.output_file.writelines("@SP\n")                     
                self.output_file.writelines("AM=M-1\n")             
                self.output_file.writelines("D=M\n")                   
                self.output_file.writelines("@%s\n" % str(num+5))
                self.output_file.writelines("M=D\n") 
                self.output_file.writelines("@SP\n") 
                self.output_file.writelines("A=M\n\n")  
                self.line += 7    
            elif segment == "pointer" :
                self.output_file.writelines("@SP\n")                     
                self.output_file.writelines("AM=M-1\n")             
                self.output_file.writelines("D=M\n")                  
                if num == 0 :
                    self.output_file.writelines("@THIS\n") 
                elif num == 1 :
                    self.output_file.writelines("@THAT\n")   
                self.output_file.writelines("M=D\n")   
                self.output_file.writelines("@SP\n") 
                self.output_file.writelines("A=M\n\n")    
                self.line += 7                          
            elif segment == "static" :
                self.output_file.writelines("@SP\n")                     
                self.output_file.writelines("AM=M-1\n")             
                self.output_file.writelines("D=M\n")                   
                self.output_file.writelines("@%s.static%s\n" % (self.filename, index))                 
                self.output_file.writelines("M=D\n")   
                self.output_file.writelines("@SP\n") 
                self.output_file.writelines("A=M\n\n")    
                self.line += 7     
            # 아래 segment는 함수 세팅 값에 따라 초기값이 달라 질 수 있기 때문에 숫자로 하드 코딩 x                                         
            else :     
                self.output_file.writelines("@%s\n" % index)   
                self.output_file.writelines("D=A\n")  
                if segment == "local" :        
                    self.output_file.writelines("@LCL\n")     
                elif segment == "argument" :         
                    self.output_file.writelines("@ARG\n")               
                elif segment == "this" :         
                    self.output_file.writelines("@THIS\n")               
                elif segment == "that" :         
                    self.output_file.writelines("@THAT\n")                
                # POP 실행    
                self.output_file.writelines("D=D+M\n")    
                self.output_file.writelines("@%s.tmp\n" % self.filename)     
                self.output_file.writelines("M=D\n")
                self.output_file.writelines("@SP\n")                     
                self.output_file.writelines("AM=M-1\n")             
                self.output_file.writelines("D=M\n")                    
                self.output_file.writelines("@%s.tmp\n" % self.filename)     
                self.output_file.writelines("A=M\n")     
                self.output_file.writelines("M=D\n")  
                self.output_file.writelines("@SP\n") 
                self.output_file.writelines("A=M\n\n")                               
                self.line += 14                
                    
    # ** label 명령어 수행 ** #
    # vm emulator를 봤을 때 별도의 스택 공간에 라인 주소를 보관하지 않음.
    # 명령은 순차적으로 진행되는데 label 명령은 순차적이지 않음.(label을 먼저 선언 안해도 분기 명령으로 먼저 사용하는 경우)
    # 컴파일러에서 명령어 라인을 자체적으로 계산한 후 label을 따로 처리 하는 것으로 추정.
    # codewriter 2번 써서 line을 계산해 label을 붙여 줄 수 있지만 수행시간이 과도해서 setlabel을 사용.
    def writelabel(self, label):
        return 0

    # ** goto 명령어 수행 ** #
    def writeGoto(self, label):
        self.output_file.writelines("@%s\n" %  str(self.LABEL[label])) 
        self.output_file.writelines("0;JMP\n")   
        self.line += 2

    # ** if-goto 명령어 수행 ** #
    def writeIf(self, label):                    
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=M-1\n")        
        self.output_file.writelines("D=M\n") 
        # 조건문 점프    
        self.output_file.writelines("@%s\n" % str(self.line + 4 + 4)) 
        self.output_file.writelines("D;JEQ\n")   
        self.output_file.writelines("@%s\n" % str(self.line + 6 + 4)) 
        self.output_file.writelines("D;JNE\n")
        # 같을 경우 
        self.output_file.writelines("@%s\n" % str(self.line + 8 + 4)) 
        self.output_file.writelines("0;JMP\n")                
        # # 다를 경우 
        self.output_file.writelines("@%s\n" %  str(self.LABEL[label])) 
        self.output_file.writelines("0;JMP\n")                      
        # 결과 반영         
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=M\n")             
        self.output_file.writelines("D=M\n\n")            
        self.line += 14

    # ** call 명령어 수행 ** #
    def writeCall(self, functionName, numArgs):
        return 0

    # ** return 명령어 수행 ** #
    def writeReturn(self):
        # LCL값과 ARG[2]값 옮기기 #
        self.output_file.writelines("@LCL\n")  
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@R13\n")
        self.output_file.writelines("M=D\n")
        self.output_file.writelines("@2\n")   
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@ARG\n")         
        self.output_file.writelines("A=M+D\n")         
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@R14\n")
        self.output_file.writelines("M=D\n")    
        # 값 반환 #
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=M-1\n")        
        self.output_file.writelines("D=M\n") 
        self.output_file.writelines("@ARG\n")
        self.output_file.writelines("A=M\n") 
        self.output_file.writelines("M=D\n") 
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=D\n") 
        # THIS, THAT, LCL, ARG, 초기화 #
        # THIS
        self.output_file.writelines("@5\n")   
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@ARG\n")         
        self.output_file.writelines("A=M+D\n")         
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@THIS\n")
        self.output_file.writelines("M=D\n")           
        # THAT
        self.output_file.writelines("@6\n")   
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@ARG\n")         
        self.output_file.writelines("A=M+D\n")         
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@THAT\n")
        self.output_file.writelines("M=D\n")         
        # LCL
        self.output_file.writelines("@3\n")   
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@ARG\n")         
        self.output_file.writelines("A=M+D\n")         
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@LCL\n")
        self.output_file.writelines("M=D\n")     
        # ARG
        self.output_file.writelines("@4\n")   
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@ARG\n")         
        self.output_file.writelines("A=M+D\n")         
        self.output_file.writelines("D=M\n")
        self.output_file.writelines("@ARG\n")
        self.output_file.writelines("M=D\n")                          
        # SP 조정 #
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=M+1\n")   
        self.line += 50



    # ** function 명령어 수행 ** #
    def writeFunction(self, functionName, numLocals):
        num = int(numLocals)
        self.functionName = functionName
        self.output_file.writelines("(%s)\n" % self.functionName) 
        self.output_file.writelines("@%s\n" % str(6))  
        self.output_file.writelines("D=A\n")     
        self.output_file.writelines("@ARG\n")               
        self.output_file.writelines("A=M+D\n")              
        self.line += 4
        # numLocals의 수 만큼 변수 초기화 #
        for i in range(0, num) :                   
            self.output_file.writelines("A=A+1\n")              
            self.output_file.writelines("M=0\n")          
            self.line += 2
        self.output_file.writelines("@%s\n" % str(i+1))
        self.output_file.writelines("D=A\n")         
        self.output_file.writelines("@SP\n")                     
        self.output_file.writelines("AM=M+D\n")   
        self.line += 4

    def setLabel(self, LABEL):
        print(LABEL)
        self.LABEL = LABEL

    # ** 파일 닫기 ** #
    def close(self):
        self.output_file.close()
