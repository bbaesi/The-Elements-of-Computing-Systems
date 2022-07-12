    @2 
    M=0 //R2 = 0
    @i
    M=1 //i=1

    (LOOP)
    @i 
    D=M //D=i
    @1 
    D=D-M // D=i-R1
    @END
    D;JGT //If (i-R1) > 0 goto End
    @0 
    D=M // D=R0
    @2
    M=D+M // R2=R2+R0 
    @i
    M=M+1 // i=i+1
    @LOOP
    0;JMP 

    (END)
    @END
    0;JMP