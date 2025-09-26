from flask import Flask, render_template, request
from lexer import lexer
from parser import parser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    entrada = ""
    tokens = {
        "palabras_reservadas": [],
        "identificadores": [],
        "numeros": [],
        "simbolos": [],
        "desconocidos": []
    }
    resultado_sintactico = None
    mostrar_lexico = False

    if request.method == "POST":
        entrada = request.form["palabra"]
        accion = request.form["accion"]  # Aquí esperamos el valor del botón pulsado

        if accion == "lexico":
            lexer.input(entrada)
            mostrar_lexico = True

            # Limpiar tokens antes de analizar
            for key in tokens:
                tokens[key] = []

            while True:
                tok = lexer.token()
                if not tok:
                    break
                # Clasificar tokens según tipo
                if tok.type == 'FOR':
                    tokens['palabras_reservadas'].append(tok.value)
                elif tok.type == 'WHILE':
                    tokens['palabras_reservadas'].append(tok.value)
                elif tok.type == 'IF':
                    tokens['palabras_reservadas'].append(tok.value)
                elif tok.type == 'IDENTIFIER':
                    tokens['identificadores'].append(tok.value)
                elif tok.type == 'NUMBER':
                    tokens['numeros'].append(str(tok.value))
                elif tok.type in ['LPAREN', 'RPAREN', 'SEMI', 'ASSIGN', 'RELOP', 'PLUSPLUS', 'LBRACE', 'RBRACE', 'DOT', 'COMMA', 'STRING']:
                    tokens['simbolos'].append(tok.value)
                elif tok.type == 'ERROR':
                    tokens['desconocidos'].append(tok.value)

        elif accion == "sintactico":
            try:
                parser.parse(entrada)
                resultado_sintactico = "✅ Sintáctico Correcto"
            except SyntaxError as e:
                resultado_sintactico = f"❌ {str(e)}"
            except Exception as e:
                # Por si hay otro tipo de error no manejado
                resultado_sintactico = f"❌ Error: {str(e)}"

    return render_template(
        "index.html",
        tokens=tokens,
        entrada=entrada,
        sintaxis=resultado_sintactico,
        mostrar_lexico=mostrar_lexico
    )

if __name__ == "__main__":
    app.run(debug=True)
