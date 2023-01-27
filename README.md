# 64-bit Graphical CPU

## CPU
### Inputs
#### Tunnels
clock - Clock input  
databus - Databus

#### Clock Control
Manual Stepping - button to switch from auto-clock to manual clock. Default high, setting to manual.  

#### Databus Control
Databus Manual Switch - Switch to manual input into the databus  

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
