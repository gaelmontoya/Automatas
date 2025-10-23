from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

def evaluate_expression(code: str):
    input_stream = InputStream(code)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)

    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    # Pedimos los números al usuario
    x = input("Ingresa x: ")
    y = input("Ingresa y: ")

    # Generamos automáticamente el código MiniLang
    user_code = (
        f"x = {x}\n"
        f"y = {y}\n"
        f"z = x * y + 10\n"
        f"print(z)\n"
        f"x = x + 1\n"
        f"print(x)\n"
    )

    try:
        evaluate_expression(user_code)
    except Exception as ex:
        print(f"Error: {ex}")