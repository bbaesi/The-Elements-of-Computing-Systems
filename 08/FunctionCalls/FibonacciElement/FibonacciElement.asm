(init)
@ARG
A=M+D
@1
D=A
@SP
AM=M+D

@4
D=A
@SP
A=M
M=D
@SP
M=M+1

@59
D=A
@SP
A=M
M=D
@SP
AM=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
AM=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
AM=M+1
D=A
@LCL
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@fibonacci
0;JMP
@61
0;JMP
(fibonacci)
@ARG
A=M+D
@1
D=A
@SP
AM=M+D

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
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
D=M-D
@96
D;JLT
@99
D;JGE
D=-1
@100
0;JMP
D=0
@SP
A=M
M=D
@SP
AM=M+1

@SP
AM=M-1
D=M
@112
D;JEQ
@114
D;JNE
@116
0;JMP
@123
0;JMP
@SP
AM=M
D=M

@183
0;JMP
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@R13
M=D
@2
D=A
@ARG
A=M+D
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
AM=D
@5
D=A
@ARG
A=M+D
D=M
@THIS
M=D
@6
D=A
@ARG
A=M+D
D=M
@THAT
M=D
@3
D=A
@ARG
A=M+D
D=M
@LCL
M=D
@4
D=A
@ARG
A=M+D
D=M
@ARG
M=D
@SP
AM=M+1

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1

@253
D=A
@SP
A=M
M=D
@SP
AM=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
AM=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
AM=M+1
D=A
@LCL
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@fibonacci
0;JMP
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
D=M
@SP
AM=M-1
M=M-D
@SP
AM=M+1

@325
D=A
@SP
A=M
M=D
@SP
AM=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
AM=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
AM=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
AM=M+1
D=A
@LCL
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@fibonacci
0;JMP
@SP
AM=M-1
D=M
D=M
@SP
AM=M-1
M=M+D
@SP
AM=M+1

@LCL
D=M
@R13
M=D
@2
D=A
@ARG
A=M+D
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
AM=D
@5
D=A
@ARG
A=M+D
D=M
@THIS
M=D
@6
D=A
@ARG
A=M+D
D=M
@THAT
M=D
@3
D=A
@ARG
A=M+D
D=M
@LCL
M=D
@4
D=A
@ARG
A=M+D
D=M
@ARG
M=D
@SP
AM=M+1

