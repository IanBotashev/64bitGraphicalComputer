# Assembly
## NOP
NOP  
Does nothing for a clock cycle  

0b00000000000000000000

## LLA
LLA {value}  
Load a literal value from next address in ROM to the A Register  

0b00000000000000000001  
## STA
STA {MEMORY ADDRESS}
Store value from the A register into the memory at a certain address.  

## ADD
ADD {memory address}  
Add a number from memory with a value in register A.  
A + ADDRESS  
0x4080
0x220
0x2108
0b00000000000000000000 (UNDEFINED YET)