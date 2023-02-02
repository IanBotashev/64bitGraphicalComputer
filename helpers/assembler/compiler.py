from helpers.assembler.tokenizer import TokenType, Token, Tokenizer
from helpers.assembler.errors import MissingInstruction


class Compiler:
    """
    Compiler turns tokens into actual, computer-readable bytecode.
    Does not spit out hex, needs to be done so by the writer.
    """
    # All the assembly instructions with their decimal number.
    # Later converted to binary.
    # Also stores their offset, if they store their parameters in addresses over.
    INSTRUCTION_SET = {
        'nop': {"value": 0, "offset": 0},
        'lla': {"value": 1, "offset": 0},
        'sta': {"value": 2, "offset": 0},
        'lda': {"value": 3, "offset": 0},
        'llb': {"value": 4, "offset": 0},
        'stb': {"value": 5, "offset": 0},
        'ldb': {"value": 6, "offset": 0},
        'sli': {"value": 7, "offset": 1},
        'add': {"value": 8, "offset": 0},
        'sub': {"value": 9, "offset": 0},
        'mul': {"value": 10, "offset": 0},
        'div': {"value": 11, "offset": 0},
        'jmp': {"value": 12, "offset": 0},
        'jez': {"value": 13, "offset": 0},
        'jen': {"value": 14, "offset": 0},
        'jgt': {"value": 15, "offset": 0},
        'jet': {"value": 16, "offset": 0},
        'jlt': {"value": 17, "offset": 0},
        'hlt': {"value": 18, "offset": 0},
    }

    def __init__(self):
        self.token_stream = []
        self.index = 0
        self.current_address = 0
        self.current_line = 0

    def compile(self, tokens):
        self.index = 0
        self.current_address = 0
        self.token_stream = tokens
        result = []

        while self.index < len(self.token_stream):
            result += self.compile_line(self.index)
            self.index += 1

        return result

    def compile_line(self, start_index):
        """
        Compiles just one line, does not go beyond a newline character.
        :param start_index: The index to start at.
        :return:
        """
        result = ""
        index = start_index
        if self.token_stream[index].t_type == TokenType.STRING:
            value = self.INSTRUCTION_SET[self.token_stream[index].t_data.lower()]['value']
            result = f"{int(value):08b}"
        else:
            raise MissingInstruction(f"Missing instruction at line {self.current_line}")

        index += 1
        while index < len(self.token_stream):


        return [result]


if __name__ == "__main__":
    tokenizer = Tokenizer()
    compiler = Compiler()
    while True:
        line = input(">")
        tokens = tokenizer.tokenize(line)
        byte = compiler.compile(tokens)

        print(byte)
