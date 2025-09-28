# parser.py
import ply.yacc as yacc
from lexer import tokens

# ----------------------------
# REGLA DE INICIO
# ----------------------------
def p_program(p):
    '''program : PROGRAMA IDENTIFIER LPAREN RPAREN LBRACE declarations statements END SEMI RBRACE'''
    p[0] = "Sintáctico Correcto"

# ----------------------------
# DECLARACIONES
# ----------------------------
def p_declarations(p):
    '''declarations : declaration declarations
                    | declaration'''
    pass

def p_declaration(p):
    '''declaration : INT identifier_list SEMI'''
    pass

def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                       | IDENTIFIER COMMA identifier_list'''
    pass

# ----------------------------
# STATEMENTS
# ----------------------------
def p_statements(p):
    '''statements : statement
                  | statement statements'''
    pass

def p_statement_read(p):
    '''statement : READ IDENTIFIER SEMI'''
    pass

def p_statement_assignment(p):
    '''statement : IDENTIFIER ASSIGN expression SEMI'''
    pass

def p_statement_printf(p):
    '''statement : PRINTF LPAREN STRING RPAREN'''
    pass

# ----------------------------
# EXPRESIONES
# ----------------------------
def p_expression_plus(p):
    '''expression : IDENTIFIER PLUS IDENTIFIER'''
    pass

def p_expression_number(p):
    '''expression : NUMBER'''
    pass

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    pass

# ----------------------------
# MANEJO DE ERRORES
# ----------------------------
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}'")
    else:
        raise SyntaxError("Error de sintaxis inesperado")

parser = yacc.yacc()