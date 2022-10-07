class Parser:

    #파일 읽기
    def __init__(self) -> None:
        pass

    #명령어 파악
    def hasMoreCommands(self):
        return 0

    #다음 명령어 읽어서 현재 명령어로
    def advance(self):
        return 0
    
    #현재 명령어 타입 반환
    def commandType(self):
        return 0

    #현재 명령어에서 기호 또는 10진수를 반환
    def symbol(self):
        return 0

    #현재 C명령(8개 종류)의 dest 연상기호를 반환
    def dest(self):
        return 0
    
    #현재 C명령(28개 종류)에서 comp 연상기호를 반환
    def comp(self):
        return 0

    #현재 C명령(8개 종류)에서 jump 연상 기호를 반환한다.
    def jump(self):
        return 0



