from dis import Instruction


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
    
    # ** 현재 명령어 타입 반환 ** #
    def commandType(self):
        if self.instructions[self.line][0] == '(':
            return 'L_COMMAND'
        if self.instructions[self.line][9] == '@':
            return 'A_COMMAND'
        return 'C_COMMAND'

    # ** 현재 명령어에서 기호 또는 10진수를 반환 ** #
    def symbol(self):
        # L_COMMAND일 경우
        if self.instructions[self.line][0] == '(':
            return self.instructions[self.line][1:-1]
        # A_COMMAN일 경우
        elif self.instructions[self.line][0] == '@':
            return self.instructions[self.line][1:]
        return print("symbol 오류")

    # ** 현재 C명령(8개 종류)의 dest 연상기호를 반환 ** #
    def dest(self):
        
        return 0
    
    # ** 현재 C명령(28개 종류)에서 comp 연상기호를 반환 ** #
    def comp(self):
        return 0

    # ** 현재 C명령(8개 종류)에서 jump 연상 기호를 반환한다. ** #
    def jump(self):
        return 0



