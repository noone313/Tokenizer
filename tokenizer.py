import re

# Define token types
token_types = [
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # identifiers (variable names, function names, etc.)
    ('NUMBER', r'\d+(\.\d+)?'),       # numbers (integers and floats)
    ('OPERATOR', r'[+\-*/]'),         # arithmetic operators
    ('ASSIGN', r'=')                  # assignment operator
]

# Tokenize function
def tokenize(code):
    tokens = []
    while code:
        code = code.strip()
        matched = False
        for token_type, pattern in token_types:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                if token_type == 'IDENTIFIER':
                    # If identifier, further classify each part
                    for c in value:
                        tokens.append(('IDENTIFIER', c))
                else:
                    tokens.append((token_type, value))
                code = code[len(value):]
                matched = True
                break
        if not matched:
            raise ValueError('Invalid input at: ' + code)
    return tokens

# Function to find and print variable name
def print_variable_name(tokens):
    variable_name = ''
    for token_type, value in tokens:
        if token_type == 'IDENTIFIER':
            variable_name += value
    if variable_name:
        print("Variable name:", variable_name)

# Main function
def main():
    code = input("Enter the code to tokenize: ")
    try:
        tokens = tokenize(code)
        print("\nTokens:")
        for token in tokens:
            print(token)
        print_variable_name(tokens)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
