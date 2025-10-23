from flask import Flask, request, jsonify, render_template
from antlr4 import InputStream, CommonTokenStream
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code", "")
    try:
        visitor = EvalVisitor()  # nuevo visitor por ejecución

        input_stream = InputStream(code)
        lexer = MiniLangLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = MiniLangParser(tokens)
        tree = parser.program()

        visitor.visit(tree)

        return jsonify({"result": visitor.output})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

