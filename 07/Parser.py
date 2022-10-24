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
        print(self.instructions)
        print("\n")
        return self.line + 1 < len(self.instructions)

    # ** 다음 명령어 읽어서 현재 명령어로 ** #
    # asm 파일 내의 주석 \\를 기준으로 '\n' 및 공백 처리.
    # .replace(" ","") -> 공백치환
    # .replace("\n", "") -> \n치환
    def advance(self):
        self.line += 1
        self.instructions[self.line] = self.instructions[self.line].split('//')[0].replace('\n','').replace(' ', '')
        # print(self.instructions[self.line])
        #공백 줄 처리 따로 안하면 list[][] 원소 호출 과정에서 IndexError 발생 한다.
        # while self.hasMoreCommands() and self.instructions[self.line] == "":
        #     self.line+=1
        #     self.instructions[self.line] = self.instructions[self.line].split('//')[0].replace('\n','').replace(' ', '')
            # print(self.instructions[self.line])
    
    # ** 현재 명령어 타입 반환 ** #
    def commandType(self):
        if self.instructions[self.line][0] == '(':
            return 'L_COMMAND'        
        if self.instructions[self.line][0] == '@':
            return 'A_COMMAND'
        return 'C_COMMAND'

    # 첫번째 인수 반환
    def arg1(self):
        return 0
    
    # 두번째 인수 반환
    def arg2(self):
        return 0