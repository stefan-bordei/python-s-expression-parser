from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        userInput = input("Enter an expression: ")
        lexer = Lexer(userInput)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()

        if not tree:
            continue

        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(f'Tree: {tree}')
        print(type(tree))
        print(value)
    except Exception as e:
        print(e)
