@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@THIS
M=D
@SP
A=M

@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@THAT
M=D
@SP
A=M

@32
D=A
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@THIS
D=D+M
@PointerTest.tmp
M=D
@SP
AM=M-1
D=M
@PointerTest.tmp
A=M
M=D
@SP
A=M

@46
D=A
@SP
A=M
M=D
@SP
M=M+1

@6
D=A
@THAT
D=D+M
@PointerTest.tmp
M=D
@SP
AM=M-1
D=M
@PointerTest.tmp
A=M
M=D
@SP
A=M

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1

@2
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1

@6
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1

