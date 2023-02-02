from enum import Enum
import string
from helpers.assembler.errors import InvalidCharacterException


class TokenType(Enum):
    """
    Simple enumerator that contains all the possible token types.
    """
    INVALID = "INVALID"  # Character which does not fit into any of the below categories.
    NEWLINE = "NEWLINE"  # Not a character. Tells compiler to begin a new line.
    STRING = "STRING"  # Basically instruction token.
    INTEGER = "INTEGER"  # Any number.
    JUMP_POINTER = "JUMP POINTER"  # A token for jump points denoted by "&". Automatically adjusts for offsets.
    IGNORE = "IGNORE"  # Characters ignored completely by the compiler.
    MULTI_SEPARATOR = "MULTI SEPARATOR"
    ONELINE_SEPARATOR = "ONE LINE SEPARATOR"


class Token:
    """
    Data class that represents a single token.
    Carries the type and data of each token.
    """

    def __init__(self, type: TokenType, data=""):
        self.t_type = type
        self.t_data = data

    def __repr__(self):
        return f"Token({self.t_type}, '{self.t_data}')"


class Tokenizer:
    """
    Tokenize raw assembly code strings.
    Returns a stream of Tokens.
    """
    # List of all possible tokens.
    TOKENIZATION = {
        # Ignored chars
        # Token Type      # All the chars it can be            # Longer than just one char?
        TokenType.IGNORE: {"characters": [" "], "string": True},
        TokenType.STRING: {"characters": string.ascii_letters, "string": True},
        TokenType.INTEGER: {"characters": string.digits, "string": True},
        TokenType.JUMP_POINTER: {"characters": ["&"], "string": False},
        TokenType.NEWLINE: {"characters": ["\n"], "string": False},
        TokenType.MULTI_SEPARATOR: {"characters": [","], "string": False},
        TokenType.ONELINE_SEPARATOR: {"characters": [":"], "string": False},
    }

    def __init__(self):
        self.index = 0

    def tokenize(self, line) -> list:
        """
        Tokenizes a string of characters
        :param line:
        :return:
        """
        result = []
        self.index = 0
        while self.index < len(line):
            data = line[self.index]
            token_type = self.get_token_type(data)

            # Check if the token type is an invalid one
            if token_type == TokenType.INVALID:
                raise InvalidCharacterException(f"Invalid Character '{data}' at position {self.index}")

            if self.TOKENIZATION[token_type]['string']:
                # Replace the one character data with this new, elongated one.
                data, index_offset = self.get_string_type(line, token_type)
                self.index += index_offset

            result.append(Token(token_type, data))
            self.index += 1

        return result

    def get_token_type(self, char) -> TokenType:
        """
        Returns what type of token a character is.
        :param char:
        :return:
        """
        for token_type in self.TOKENIZATION:  # Dictionary fuckery, don't worry about it
            if char in self.TOKENIZATION[token_type]['characters']:
                return token_type

        return TokenType.INVALID

    def get_string_type(self, line, type: TokenType) -> (str, int):
        """
        Get types denoted with "string".
        Finds the sequence of characters with the same type, and returns their overall value.
        :param type: Type of token to look for.
        :param line: Cut line. Starts from the start of a stringed token.
        :return:
        """
        # We need to know the index to know how to split the string, and how much to offset in the tokenize method.
        string_index = self.index + 1
        while string_index < len(line):  # Go through each character
            if self.get_token_type(line[string_index]) != type:
                break

            string_index += 1

        return line[self.index:string_index], string_index - self.index - 1


if __name__ == "__main__":
    tokenizer = Tokenizer()
    while True:
        line_ = input('>')
        print(" ", tokenizer.tokenize(line_))
