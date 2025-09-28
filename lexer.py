import ply.lex as lex

tokens = (
    'FOR', 'WHILE', 'IF',
    'IDENTIFIER', 'NUMBER',
    'PLUS', 'MINUS', 'ASSIGN', 'RELOP',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMI', 'DOT', 'COMMA', 'STRING'
)

reserved = {
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF'
}

t_PLUS = r'\+'
t_MINUS = r'\-'
t_ASSIGN = r'='
t_RELOP = r'==|!=|<=|>=|<|>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_DOT = r'\.'
t_COMMA = r','

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# ✅ Manejo real de errores léxicos
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()