import json


instructions = {
    "IRw": 0,
    "ROMr": 0,
    "PAinc": 0,
    "CCclr": 0,
    "PAw": 0,
    "RAMr": 0,
    "RAMw": 0,
    "ADDRw": 0,
    "SRr": 0,
    "SRw": 0,
    "RBr": 0,
    "RBw": 0,
    "RAr": 0,
    "RAw": 0,
    "DBout": 0,
    "ALUop": "0000",
    "CPAw": "000",
    "HLT": 0,
}


def main():
    file = input("file: ")
    with open(file, 'r') as f:
        file = json.load(f)
        values = file["values"]
        for value in values:
            instructions_copy = instructions.copy()
            instructions_copy.update(value)
            print(f"0b{''.join(str(e) for e in reversed(instructions_copy.values()))}")


if __name__ == "__main__":
    main()
