class Parser:

    # ** 파일 읽기 ** #
    def __init__(self, path):
        self.path = path
        input_file = open(path,'r')
        self.instructions = input_file.readlines()
        input_file.close()
        self.line = -1

    # ** 명령어 파악 ** #
    def hasMoreCommands(self):
        # print(self.instructions)
        # print("\n")
        return self.line + 1 < len(self.instructions)

    # ** 다음 명령어 읽어서 현재 명령어로 ** #
    # asm 파일 내의 주석 \\를 기준으로 '\n' 및 공백 처리.
    # .replace(" ","") -> 공백치환
    # .replace("\n", "") -> \n치환
    def advance(self):
        self.line += 1
        self.instructions[self.line] = self.instructions[self.line].split('//')[0].replace('\n','')
        #공백 줄 처리 따로 안하면 list[][] 원소 호출 과정에서 IndexError 발생 한다.
        while self.hasMoreCommands() and self.instructions[self.line] == "":
            self.line+=1
            self.instructions[self.line] = self.instructions[self.line].split('//')[0].replace('\n','')
    
    # ** 현재 명령어 타입 반환 ** #
    def commandType(self):
        command = self.instructions[self.line].split(' ')[0]
        if command != '' :
            if command in 'push' :
                return 'C_PUSH'        
            elif command in 'pop' :
                return 'C_POP'
            elif command in 'label' :
                return 'C_LABEL'
            elif command in 'goto' :
                return 'C_GOTO'
            elif command in 'if' :
                return 'C_IF'
            elif command in 'function' :
                return 'C_FUNCTION'                 
            elif command in 'return' :
                return 'C_RETURN'                                                
            elif command in 'call' :
                return 'C_CALL'              
            return 'C_ARITHMETIC'   

    # 첫번째 인수 반환
    def arg1(self):  

        if self.commandType() != "C_RETURN" :
            if self.commandType() == "C_ARITHMETIC" :
                return self.instructions[self.line].split(' ')[0]
            else :
                return self.instructions[self.line].split(' ')[1]
    
    # 두번째 인수 반환
    def arg2(self):
        if self.commandType() == "C_PUSH" or self.commandType() == "C_POP" or  self.commandType() == "C_FUNCTION" or self.commandType() == "C_CALL" :
            return self.instructions[self.line].split(' ')[2]