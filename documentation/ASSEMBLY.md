# Assembly
Each instruction is 20 bits of a full 64
## NOP
NOP  
Does nothing for a clock cycle  

0b00000000000000000000 (0)

## LLA
LLA {value}  
Load a literal value from next address in ROM to the A Register  

0b00000000000000000001 (1)  
## STA
STA {MEMORY ADDRESS}  
Store value from the A register into the memory at a certain address.  

0b00000000000000000010 (2)  
## LDA
LDA {MEMORY ADDRESS}  
Load a value from memory into the A register.   
Memory Address is on the same line after the first 20 bits

0b00000000000000000011 (3)  

## LLB
LLB {value}  
Load a literal value from next address in ROM to the B Register  

0b00000000000000000100 (4)  
## STB
STB {MEMORY ADDRESS}  
Store value from the B register into the memory at a certain address.  

0b00000000000000000101 (5)
## LDB
LDB {MEMORY ADDRESS}  
Load a value from memory into the B register.   
Memory Address is on the same line after the first 20 bits

0b00000000000000000110 (6)  

## SLI
SLI {MEMORY ADDRESS}, {VALUE}
Store Literal, stores a value from ROM into the RAM. Memory Address on same line,  
Value to store on the next address.  

0b00000000000000000111 (7) 

## ADD
ADD {memory address}  
Add a number from memory with a value in register A. Memory Address is on the same line.  
A + ADDRESS  

0b00000000000000001000 (8)

## SUB
SUB {memory address}
Subtract a number from memory with a value in Register. Memory Address is on the same line.  
A - ADDRESS  

0b00000000000000001001 (9)

## MUL
MUL {memory address}
Multiply a number from memory with a value in Register. Memory Address is on the same line.  
A * ADDRESS  

0b00000000000000001010 (10)

## DIV
DIV {memory address}
Divide a number from memory with a value in Register. Memory Address is on the same line.  
A / ADDRESS  

0b00000000000000001011 (11)

## JMP
DIV {memory address}
Jump to that memory address in the ROM 

0b00000000000000001100 (12)