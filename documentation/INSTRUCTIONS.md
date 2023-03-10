# Instructions
The first 8 bits of the 64 in the ROM are for instructions.  
The 56 left over bits are for arguments.

## Microinstructions
25 bits out  
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
HLT
D1out
D2out

## Explanations
IRw - Instruction Register Write. Outputs to the control logic  
ROMr - Output the contents of the ROM to the databus  
  
PAinc - Program Address Increment. Increments the address by one for the ROM on the next clock cycle  
PAw - Program Address write. Takes from databus  
CPAw - Conditional Address Write.
0. inactive
1. Greater Than  
2. Equal To  
3. Lesser Than  
4. Zero
5. Negative
  
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

HLT - Halts clock from further cycles.

DBout - Outputs everything but the instruction onto the databus.
D1out - Outputs first half of DBout onto the databus
D2out - Outputs second half of DBout onto the databus