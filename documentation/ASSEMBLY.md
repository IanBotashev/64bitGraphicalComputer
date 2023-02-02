# Assembly
Each instruction is 8 bits of a full 64  
Leaving 56 bits for arguments

## NOP
NOP  
Does nothing for a clock cycle  

0b00000000 (0)

## LLA
LLA {value}  
Load a literal value from next address in ROM to the A Register  

0b00000001 (1)  
## STA
STA {memory address}  
Store value from the A register into the memory at a certain address.  

0b00000010 (2)  
## LDA
LDA {memory address}  
Load a value from memory into the A register.   
Memory Address is on the same line after the first 20 bits

0b000000011 (3)  

## LLB
LLB {value}  
Load a literal value from next address in ROM to the B Register  

0b00000100 (4)  
## STB
STB {memory address}  
Store value from the B register into the memory at a certain address.  

0b00000101 (5)
## LDB
LDB {memory address}  
Load a value from memory into the B register.   
Memory Address is on the same line after the first 20 bits

0b00000110 (6)  

## SLI
SLI {memory address}, {value}
Store Literal, stores a value from ROM into the RAM. Memory Address on same line,  
Value to store on the next address.  

0b000000111 (7) 

## ADD
ADD {memory address}  
Add a number from memory with a value in register A. Memory Address is on the same line.  
A + ADDRESS  

0b00001000 (8)

## SUB
SUB {memory address}
Subtract a number from memory with a value in Register. Memory Address is on the same line.  
A - ADDRESS  

0b00001001 (9)

## MUL
MUL {memory address}
Multiply a number from memory with a value in Register. Memory Address is on the same line.  
A * ADDRESS  

0b00001010 (10)

## DIV
DIV {memory address}
Divide a number from memory with a value in Register. Memory Address is on the same line.  
A / ADDRESS  

0b00001011 (11)

## JMP
JMP {memory address}
Jump to that memory address in the ROM 

0b00001100 (12)

## JEZ
JEZ {memory address}
Jump to that memory address in the ROM if the last operation in the ALU equaled zero.  

0b00001101 (13)

## JEN
JEN {memory address}
Jump to that memory address in the ROM if the last operation in the ALU is negative.  

0b00001110 (14)

## JGT
JGT {jump address}:{compare address}  
Evaluate if register A value > the value in the memory address, if true, jump.  
Jump and Compare addresses on same line, following split databus formatting    

0b00001111 (15)

## JET
JET {jump address}:{compare address}  
Evaluate if register A value == the value in the memory address, if true, jump.  
Jump and Compare addresses on same line, following split databus formatting  

0b00010000 (16)

## JLT
JLT {jump address}:{compare address}  
Evaluate if register A value < the value in the memory address, if true, jump.  
Jump and Compare addresses on same line, following split databus formatting  

0b00010001 (17)

## HLT
HLT 
Halt the clock.

0b00010010 (18)
