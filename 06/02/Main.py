from curses.ascii import isdigit
import sys
import SymbolTable
import Parser
import Code


def main():
    # 객체 선언 
    first_parser = Parser.Parser(sys.argv[1])
    second_parser = Parser.Parser(sys.argv[1])
    symbolTable = SymbolTable.SymbolTable()
    code = Code.Code()
     
    # 파일 열기
    output = sys.argv[1].split('.asm')[0] + '.hack'
    hack = open(output, "a")

    # ROM 주소 기록하는 변수
    address_counter = 0
    new_address = 16

    #첫번째 파싱
    while first_parser.hasMoreCommands():
        first_parser.advance()
        if first_parser.commandType() == "L_COMMAND" :
            symbol = first_parser.symbol()
            symbolTable.addEntry(symbol,address_counter)   
        else: 
            address_counter += 1   

    #두번째 파싱
    while second_parser.hasMoreCommands():
        second_parser.advance()
        if second_parser.commandType() == "A_COMMAND" : 
            symbol = second_parser.symbol()
            if symbol.isdigit():
                A_COMMAND = bin(int(second_parser.symbol()))[2:]
            else:
                if not symbolTable.contains(symbol):
                    symbolTable.addEntry(symbol,new_address)
                    new_address += 1      
                address = symbolTable.getAddress(symbol)
                A_COMMAND = bin(int(address))[2:]
            COMMAND = A_COMMAND.zfill(16)

        if second_parser.commandType() == "C_COMMAND" :
            comp = code.comp(second_parser.comp())
            dest = code.dest(second_parser.dest()) 
            jump = code.jump(second_parser.jump())
            COMMAND= "111"+comp+dest+jump

        if second_parser.commandType() != "L_COMMAND" :
                hack.writelines(COMMAND+"\n") 

    #파일 닫기    
    hack.close()

if __name__ == "__main__":
    main()