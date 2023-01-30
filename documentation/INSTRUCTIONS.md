# Instructions
The first 20 bits of the 64 in the ROM are for instructions.  
The 44 left over bits are for arguments.

## Microinstructions
21 bits out  
Exact Order:  
IRw  
ROMr  
PAinc  
CCclr  
PAw  
RAMr  
RAMw  
ADDRw  
SRr  
SRw  
RBr  
RBw  
RAr  
RAw  
DBout  
ALUop (4 bits)  
CPAw (3 bits)

## Explanations
IRw - Instruction Register Write. Outputs to the control logic  
ROMr - Output the contents of the ROM to the databus  
  
PAinc - Program Address Increment. Increments the address by one for the ROM on the next clock cycle  
PAw - Program Address write. Takes from databus  
CPAw - Conditional Address Write.
0. Greater Than  
1. Equal To  
2. Lesser Than  
3. Zero
4. Negative
  
CCclr - Reset Control Counter to 0.

RAw - Register A write. Writes to register from databus (1 bit)  
RAr - Register A read. Outputs value to databus (1 bit)  

RBw - Register B write. Writes to register from databus (1 bit)  
RBr - Register B read. Outputs value to databus (1 bit)  

SRw - Sum Register write. Writes from ALU to sum register (1 bit)  
SRr - Sum Register read. Outputs value to databus (1 bit)  
ALUop - Operation to perform. (4 bits)  

ADDRw - Addres Register Write. Takes 16 bits from databus and stores it (1 bit)  
RAMw - RAM write. Writes from databus at specified address (1 bit)  
RAMr - RAM read. Outputs value to databus (1 bit)
