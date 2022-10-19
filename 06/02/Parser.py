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
        #공백 줄 처리 따로 안하면 list[][] 원소 호출 과정에서 IndexError 발생 한다.
        while self.hasMoreCommands() and self.instructions[self.line] == "":
            self.line+=1
            self.instructions[self.line] = self.instructions[self.line].split('//')[0].replace('\n','').replace(' ', '')
    
    # ** 현재 명령어 타입 반환 ** #
    def commandType(self):
        if self.instructions[self.line][0] == '(':
            return 'L_COMMAND'        
        if self.instructions[self.line][0] == '@':
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
    # destination 필드, 3비트로 이루어진 저장 주소를 의미
    def dest(self):
        if self.instructions[self.line].find('=') >= 0 :
            return self.instructions[self.line].split('=')[0] 
        else: return "null"
    
    # ** 현재 C명령(28개 종류)에서 comp 연상기호를 반환 ** #
    # computation 필드, 7비트로 이루어진 함수 명령
    def comp(self):
        if self.instructions[self.line].find('=') >= 0 :
            return self.instructions[self.line].split('=')[1].split(';')[0]
        else: return self.instructions[self.line].split(';')[0]

    # ** 현재 C명령(8개 종류)에서 jump 연상 기호를 반환한다. ** #
    # jump 필드, 3비트로 이루어진 점프 조건
    def jump(self):
        if self.instructions[self.line].find(';') >= 0 :
            return self.instructions[self.line].split(';')[1]
        else: return "null"



