# lexer.py
import ply.lex as lex

tokens = (
    'FOR',
    'WHILE',
    'IF',
    'IDENTIFIER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'SEMI',
    'ASSIGN',
    'RELOP',
    'PLUSPLUS',
    'LBRACE',
    'RBRACE',
    'DOT',
    'COMMA',
    'STRING',
)

reserved = {
    'for': 'FOR',
    'while': 'WHILE',  # Puedes ajustar según necesites
    'if': 'IF'
}

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMI      = r';'
t_ASSIGN    = r'='
t_RELOP     = r'>=|<=|<|>|==|!='
t_PLUSPLUS  = r'\+\+'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_DOT       = r'\.'
t_COMMA     = r','

t_ignore = ' \t'

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.type = 'ERROR'
    return t

lexer = lex.lex()