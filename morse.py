#!/usr/bin/python

import sys

# ▄ !

dit = '·'
dah = '-'

code = {

    # Basic ASCII alphabet
    'A' : dit + dah,                'B' : dah + dit + dit + dit,
    'C' : dah + dit + dah + dit,    'D' : dah + dit + dit,
    'E' : dit,                      'F' : dit + dit + dah + dit,
    'G' : dah + dah + dit,          'H' : dit + dit + dit + dit,
    'I' : dit + dit,                'J' : dit + dah + dah + dah,
    'K' : dah + dit + dah,          'L' : dit + dah + dit + dit,
    'M' : dah + dah,                'N' : dah + dit,
    'O' : dah + dah + dah,          'P' : dit + dah + dah + dit,
    'Q' : dah + dah + dit + dah,    'R' : dit + dah + dit,
    'S' : dit + dit + dit,          'T' : dah,
    'U' : dit + dit + dah,          'V' : dit + dit + dit + dah,
    'W' : dit + dah + dah,          'X' : dah + dit + dit + dah,
    'Y' : dah + dit + dah + dah,    'Z' : dah + dah + dit + dit,

    # Digits
    '1' : dit + dah + dah + dah + dah,
    '2' : dit + dit + dah + dah + dah,
    '3' : dit + dit + dit + dah + dah,
    '4' : dit + dit + dit + dit + dah,
    '5' : dit + dit + dit + dit + dit,
    '6' : dah + dit + dit + dit + dit,
    '7' : dah + dah + dit + dit + dit,
    '8' : dah + dah + dah + dit + dit,
    '9' : dah + dah + dah + dah + dit,
    '0' : dah + dah + dah + dah + dah,

    # Punctuation
    '.' : dit + dah + dit + dah + dit + dah,
    ',' : dah + dah + dit + dit + dah + dah,
    '?' : dit + dit + dah + dah + dit + dit,
    "'" : dit + dah + dah + dah + dah + dit,
    '!' : dah + dit + dah + dit + dah + dah,
    '/' : dah + dit + dit + dah + dit,
    '(' : dah + dit + dah + dah + dit,
    ')' : dah + dit + dah + dah + dit + dah,
    '&' : dit + dah + dit + dit + dit,
    ':' : dah + dah + dah + dit + dit + dit,
    ';' : dah + dit + dah + dit + dah + dit,
    '=' : dah + dit + dit + dit + dah,
    '+' : dit + dah + dit + dah + dit,
    '-' : dah + dit + dit + dit + dit + dah,
    '_' : dit + dit + dah + dah + dit + dah,
    '"' : dit + dah + dit + dit + dah + dit,
    '$' : dit + dit + dit + dah + dit + dit + dah,
    '@' : dit + dah + dah + dit + dah + dit,

    #　Spanish
    'Ñ' : dah + dah + dit + dah + dah

    # There are no prosigns yet because I haven't figured out
    # how to implement them here under single-character keys (=
}


def encode( message ):

    codified = ''

    for i, letter in enumerate( message.upper() ):

        # Three spaces to sepparate words
        if letter == ' ':
            codified += '   '
        else:
            # Single space to sepparate letters
            if i > 0 and message[i-1] != ' ':
                codified += ' '
            try:
                codified += code[letter]
            except:
                codified += '?'

    return codified


print( encode( ' '.join( sys.argv[1:] ) ) )
