# parser.py
import ply.yacc as yacc
from lexer import tokens

# Regla de inicio
def p_program(p):
    '''program : control_structure'''
    p[0] = "Sintáctico Correcto"

# Aceptar cualquiera de las estructuras
def p_control_structure(p):
    '''control_structure : for_loop
                         | while_loop
                         | if_statement'''
    pass

# ----------------
# FOR LOOP
# ----------------
def p_for_loop(p):
    '''for_loop : FOR LPAREN assignment SEMI condition SEMI increment RPAREN block'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN NUMBER'''
    pass

def p_condition(p):
    '''condition : IDENTIFIER RELOP NUMBER'''
    pass

def p_increment(p):
    '''increment : IDENTIFIER PLUS'''
    pass

# ----------------
# WHILE LOOP
# ----------------
def p_while_loop(p):
    '''while_loop : WHILE LPAREN condition RPAREN block'''
    pass

# ----------------
# IF STATEMENT
# ----------------
def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN block'''
    pass

# ----------------
# COMMON BLOCK
# ----------------
def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    pass

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    pass

def p_statement(p):
    '''statement : IDENTIFIER DOT IDENTIFIER LPAREN STRING COMMA IDENTIFIER RPAREN SEMI'''
    pass

# ----------------
# ERROR HANDLING
# ----------------
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}'")
    else:
        raise SyntaxError("Error de sintaxis inesperado")

parser = yacc.yacc()