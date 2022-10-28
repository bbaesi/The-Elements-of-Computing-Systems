class CodeWriter:

    # ** CodeWriter 기록 준비 ** #
    def __init__(self, path):
        self.path = path
        self.filename = self.path.split('.vm')[0]
        self.file = self.filename + '.asm'
        self.output_file = open(self.file,'w')   
        self.line = -1 
        self.start = 0      

    # ** 산술 명령 어셈블리 코드 기록 ** #
    def writerArithmetic(self, command):   
        if command != "neg" and command != "not" :              
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.line += 2
        if command != "and" and command != "add" and command != "sub":              
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.line += 2            

        if command == "add" :
            self.output_file.writelines("D=M\n\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")                 
            self.output_file.writelines("M=M+D\n\n")
            self.line += 4          
        elif command == "sub" :
            self.output_file.writelines("D=M\n\n")   
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")                            
            self.output_file.writelines("M=M-D\n\n")     
            self.line += 4
        elif command == "neg" :   
            self.output_file.writelines("M=-M\n\n")  
            self.line += 1
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
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")
            self.output_file.writelines("M=D\n\n")  
            self.line += 12
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
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")            
            self.output_file.writelines("M=D\n\n")  
            self.line += 12
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
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("A=M\n")            
            self.output_file.writelines("M=D\n\n")  
            self.line += 12          
        elif command == "and" :   
            self.output_file.writelines("D=M\n")      
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("AM=M-1\n")  
            self.output_file.writelines("M=M&D\n\n")
            self.line += 4          
        elif command == "or" : 
            self.output_file.writelines("M=M|D\n\n") 
            self.line += 1     
        elif command == "not" : 
            self.output_file.writelines("M=!M\n\n")   
            self.line += 1
        
        self.output_file.writelines("@SP\n")
        self.output_file.writelines("AM=M+1\n")                            
        self.line += 2                 
      

    # ** command 번역 후 어셈블리 코드 기록 ** #
    def WritePushPop(self, command, segment, index):
        num = int(index) 
        # ** PUSH case ** #        
        if command == "C_PUSH":
            if segment == "constant" :
                self.output_file.writelines("@%s\n" % str(num))  
                self.output_file.writelines("D=A\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")
            elif segment == "local" :
                self.output_file.writelines("@%s\n" % str(num+300))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")                
            elif segment == "argument" :
                self.output_file.writelines("@%s\n" % str(num+400))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")
            elif segment == "this" :
                self.output_file.writelines("@%s\n" % str(num+3000))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")
            elif segment == "that" :
                self.output_file.writelines("@%s\n" % str(num+3010))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")                                
            elif segment == "temp" :
                self.output_file.writelines("@%s\n" % str(num+5))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")
            elif segment == "pointer" :
                if num == 0 :
                    self.output_file.writelines("@%s\n" % str(3))   
                elif num == 1 :
                    self.output_file.writelines("@%s\n" % str(4))   
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")      
            elif segment == "static" :
                self.output_file.writelines("@%s\n" % str(num+16))  
                self.output_file.writelines("D=M\n")
                self.output_file.writelines("@SP\n")
                self.output_file.writelines("A=M\n")
                self.output_file.writelines("M=D\n")                          
            self.output_file.writelines("@SP\n")
            self.output_file.writelines("M=M+1\n\n")  
            self.line += 7  
                                   

        # ** POP case ** #     
        if command == "C_POP":
            # POP 준비 #
            self.output_file.writelines("@SP\n")                     
            self.output_file.writelines("AM=M-1\n")             
            self.output_file.writelines("D=M\n")               
            if segment == "constant" :             
                self.line += 0           
            elif segment == "local" :        
                self.output_file.writelines("@%s\n" % str(num+300))   
                self.output_file.writelines("M=D\n")                 
            elif segment == "argument" :         
                self.output_file.writelines("@%s\n" % str(num+400))    
                self.output_file.writelines("M=D\n")            
            elif segment == "this" :         
                self.output_file.writelines("@%s\n" % str(num+3000))  
                self.output_file.writelines("M=D\n")     
            elif segment == "that" :         
                self.output_file.writelines("@%s\n" % str(num+3010))   
                self.output_file.writelines("M=D\n")       
            elif segment == "temp" :
                self.output_file.writelines("@%s\n" % str(num+5))    
                self.output_file.writelines("M=D\n")         
            elif segment == "pointer" :
                if num == 0 :
                    self.output_file.writelines("@3\n") 
                elif num == 1 :
                    self.output_file.writelines("@4\n")
                self.output_file.writelines("M=D\n")
            elif segment == "static" :
                self.output_file.writelines("@%s\n" % str(num+16))  
                self.output_file.writelines("M=D\n")                                          
            # SP 원위치    
            self.output_file.writelines("@SP\n") 
            self.output_file.writelines("A=M\n\n")                               
            self.line += 7                       
            


    # ** 파일 닫기 ** #
    def close(self):
        self.output_file.close()
