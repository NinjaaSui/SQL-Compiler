import re

# Token specifications
token_specs = [
    ('CREATE', r'CREATE'),
    ('TABLE', r'TABLE'),
    ('INSERT', r'INSERT'),
    ('INTO', r'INTO'),
    ('VALUES', r'VALUES'),
    ('SELECT', r'SELECT'),
    ('FROM', r'FROM'),
    ('TYPE', r'int|varchar'),  # Place TYPE before IDENTIFIER
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('L_PAREN', r'\('),
    ('R_PAREN', r'\)'),
    ('COMMA', r','),
    ('STRING', r'\'[^\']*\''),
    ('NUMBER', r'\d+'),
    ('WHITESPACE', r'\s+'),
    ('SEMICOLON', r';'),
]

# Tokenizer using regular expressions
def lexer(input_code):
    token_specification = [(name, re.compile(pattern)) for name, pattern in token_specs]
    position = 0
    tokens = []

    while position < len(input_code):
        match = None
        for name, pattern in token_specification:
            regex = pattern.match(input_code, position)
            if regex:
                text = regex.group(0)
                if name != 'WHITESPACE':  # Skip whitespace
                    tokens.append((name, text))
                position += len(text)
                break
        else:
            raise SyntaxError(f"Illegal character {input_code[position]} at position {position}")

    return tokens