class CodeWriter:

    # ** CodeWriter 기록 준비 ** #
    def __init__(self, path):
        self.path = path
        self.stackPointer = 255
        self.filename = self.path.split('.vm')[0] + '.asm'
        self.output_file = open(self.filename,'w')   
        self.line = -1        

    # ** 산술 명령 어셈블리 코드 기록 ** #
    def writerArithmetic(self, command):   
        if command != "neg" and command != "not" :              
            self.stackPointer-=1       
        if command != "and" :              
            self.output_file.writelines("@" + str(self.stackPointer)+"\n")
        self.line += 1
        if command == "add" :
            self.output_file.writelines("M=M+D\n")
        elif command == "sub" :
            self.output_file.writelines("M=M-D\n")     
        elif command == "neg" :   
            self.output_file.writelines("M=-M\n")  
        elif command == "eq" : 
            # 조건문 점프 #
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@" + str(self.line + 2 + 4)+"\n") 
            self.output_file.writelines("D;JEQ\n")   
            self.output_file.writelines("@" + str(self.line + 4 + 5)+"\n")
            self.output_file.writelines("D;JNE\n")
            # 같을 경우 #
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@" + str(self.line + 7 + 3)+"\n")
            self.output_file.writelines("0;JMP\n")   
            # 다를 경우 #
            self.output_file.writelines("D=0\n")  
            # 결과 반영 #
            self.output_file.writelines("@" + str(self.stackPointer)+"\n")
            self.output_file.writelines("M=D\n")  
            self.line += 10
        elif command == "gt" : 
            # 조건문 점프 #
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@" + str(self.line + 2 + 4)+"\n") 
            self.output_file.writelines("D;JGT\n")   
            self.output_file.writelines("@" + str(self.line + 4 + 5)+"\n")
            self.output_file.writelines("D;JLE\n")       
            # 클 경우 #
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@" + str(self.line + 7 + 3)+"\n")
            self.output_file.writelines("0;JMP\n")   
            # 같을 경우 + 작을 경우 #
            self.output_file.writelines("D=0\n")
            # 결과 반영 #
            self.output_file.writelines("@" + str(self.stackPointer)+"\n")
            self.output_file.writelines("M=D\n")  
            self.line += 10
        elif command == "lt" : 
            # 조건문 점프 #
            self.output_file.writelines("D=M-D\n") 
            self.output_file.writelines("@" + str(self.line + 2 + 4)+"\n") 
            self.output_file.writelines("D;JLT\n")   
            self.output_file.writelines("@" + str(self.line + 4 + 5)+"\n")
            self.output_file.writelines("D;JGE\n")       
            # 클 경우 #
            self.output_file.writelines("D=-1\n")            
            self.output_file.writelines("@" + str(self.line + 7 + 3)+"\n")
            self.output_file.writelines("0;JMP\n")   
            # 같을 경우 + 작을 경우 #
            self.output_file.writelines("D=0\n")
            # 결과 반영 #
            self.output_file.writelines("@" + str(self.stackPointer)+"\n")
            self.output_file.writelines("M=D\n")  
            self.line += 10            
        elif command == "and" :   
            self.output_file.writelines("D=M\n")      
            self.output_file.writelines("@" + str(self.stackPointer)+"\n")
            self.output_file.writelines("M=M&D\n")
            self.line += 2          
        elif command == "or" : 
            self.output_file.writelines("M=M|D\n")      
        elif command == "not" : 
            self.output_file.writelines("M=!M\n")     
        self.line += 1                 
      

    # ** command 번역 후 어셈블리 코드 기록 ** #
    def WritePushPop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant" :
                self.stackPointer+=1
                self.output_file.writelines("@" + index +"\n")
                self.output_file.writelines("D=A" + "\n")
                self.output_file.writelines("@" + str(self.stackPointer)+"\n")
                self.output_file.writelines("M=D" + "\n")
                self.line += 4
        if command == "C_POP":
            if segment == "constant" :
                self.output_file.writelines("D=M" + "\n")
                self.output_file.writelines("M=0" + "\n")
                self.output_file.writelines("@" + str(self.stackPointer)+"\n")
                self.line += 4                

    # ** 파일 닫기 ** #
    def close(self):
        self.output_file.close()
