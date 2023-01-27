# 64-bit Graphical CPU
Uses ["Digital"](https://github.com/hneemann/Digital) by hneeman
## CPU
### Inputs
#### Tunnels
clock - Clock input  
databus - Databus

#### Clock Control
Manual Stepping - button to switch from auto-clock to manual clock. Default high, setting to manual.  

#### Databus Control
Databus Manual Switch - Switch to manual input into the databus  

#### Microinstructions
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

## ALU
### Inputs
A - Number A (64 bit)  
B - Number B (64 bit)  
Operation - Operation to perform (4 bit)  

### Outputs
X - Output number after operation  (64 bit)  
overflow - Overflow flag, high if overflow occurred. (1 bit)  
#### Conditional Flags
Lesser Than - High if A < B  (1 bit)  
Equal To - High if A == B  (1 bit)  
Greater Than - High if A > B  (1 bit)  

### Operations
0000 - Add  
0001 - Subtract  
0010 - Multiply (Takes the first 32 bits of A and B)  
0011 - Divide  
0100..1111 - Empty, constant low
