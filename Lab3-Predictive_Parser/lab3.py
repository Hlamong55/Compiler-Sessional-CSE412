ID = 0
CONST = 1
MULOP = 2
ADDOP = 3
OP = 4
CP = 5
ERR = 6
COL = 7

lexbuff = ""
lookahead = 0
token = -1


def parser():
    global lookahead
    lookahead = 0

    if E() and lookahead >= len(lexbuff):
        print("valid string")
    else:
        print("invalid string")


def E():
    if T():
        return EPRIME()
    return False


def T():
    if F():
        return TPRIME()
    return False


def EPRIME():
    global lookahead

    save = lookahead
    token = lexer()

    if token == ADDOP:
        if T():
            return EPRIME()
        return False

    lookahead = save
    return True


def TPRIME():
    global lookahead

    save = lookahead
    token = lexer()

    if token == MULOP:
        if F():
            return TPRIME()
        return False

    lookahead = save
    return True


def F():
    global lookahead

    token = lexer()

    if token == ID:
        return True

    elif token == OP:
        if E():
            token = lexer()
            if token == CP:
                return True

    return False


def lexer():
    global lookahead, lexbuff

    while lookahead < len(lexbuff) and lexbuff[lookahead] in (' ', '\t'):
        lookahead += 1

    if lookahead >= len(lexbuff):
        return COL

    current_char = lexbuff[lookahead]

    if current_char.isalpha():
        while lookahead < len(lexbuff) and lexbuff[lookahead].isalnum():
            lookahead += 1
        return ID

    elif current_char.isdigit():
        while lookahead < len(lexbuff) and lexbuff[lookahead].isdigit():
            lookahead += 1
        return CONST

    elif current_char == '+':
        lookahead += 1
        return ADDOP

    elif current_char == '*':
        lookahead += 1
        return MULOP

    elif current_char == '(':
        lookahead += 1
        return OP

    elif current_char == ')':
        lookahead += 1
        return CP

    else:
        lookahead += 1
        return ERR


# Read Input From File

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "input.txt")

try:
    with open(input_file, "r") as f:
        lexbuff = f.readline().strip()

    print("Input:", lexbuff)
    parser()

except FileNotFoundError:
    print("input.txt not found!")