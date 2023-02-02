# Assembler
A simple python package developed for the CPU to easily compile assembly code into bytecode for the CPU.

## Types
- **INVALID** - Any characters that don't fit into the categories. Throws an exception.
- **NEWLINE** - Tells the compier there's a new line, and to interpret everything past this as a new instruction.
- **STRING** - Currently just referring to instructions. General name incase for the future.
- **INTEGER** - Any number.
- **JUMP_POINTER** - Pointers specifically made for jump instructions. Automatically adjusts for offsets that can come with certain instructions
- **IGNORE** - Characters ignored by the compiler.
- **MULTI_SEPARATOR** - Means that the arguments should be packaged on different lines. 
- **ONELINE_SEPARATOR** = Means that there's only 2 arguments, and they should be on the same line.