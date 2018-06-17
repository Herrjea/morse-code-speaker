# ruido para los caracteres desconocidos


#!/usr/bin/python

import sys                      # comand line arguments
import pyaudio                  # Generate beeping sounds
from random import uniform      # Generate random noise values
import numpy as np

# ▄ !

dit = '·'
dah = '-'
unknown = '?'

path = 'sounds/'

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
                codified += unknown

    return codified



message = encode( ' '.join( sys.argv[1:] ) )

print( message )



## Making it speak ##


player = pyaudio.PyAudio()

speed = 1
volume = 0.5
samplingRate = 44100
frequency = 880.0
noiseBaseFrequency = 27.5
noiseFactor = 0.1

# Durations of both sounds and silences
ditDuration = .3
dahDuration = ditDuration * 3


def generateSample( duration, frequency = 800 ):

    samples = (
        np.sin(
            2 * np.pi * np.arange( samplingRate * duration ) * frequency / samplingRate
        )
    ).astype( np.float32 )

    return samples

def randomizeSample( sample, factor ):

    for i in range(len(sample)):
        sample[i] += uniform( -factor, factor )
        if sample[i] > 1:
            sample[i] = 1
        elif sample[i] < -1:
            sample[i] = 1

    return sample


# Getting ready to sing

stream = player.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = samplingRate,
    output = True
)


# Checking class notes again before the audition

ditSound = generateSample( ditDuration / speed, frequency )
dahSound = generateSample( dahDuration / speed, frequency )
noise = randomizeSample( generateSample( dahDuration / speed, noiseBaseFrequency ), noiseFactor )
shortPause = ditSound * 0
longPause = dahSound * 0


def playDit():
    stream.write( volume * ditSound )

def playDah():
    stream.write( volume * dahSound )

def playNoise():
    stream.write( volume * noise )

def playBetweenLetters():
    stream.write( shortPause )

def playBetweenWords():
    stream.write( longPause )


def playWord( word ):

    for letter in word:
        if letter == dit:
            playDit()
        elif letter == dah:
            playDah()
        elif letter == unknown:
            playNoise()
        playBetweenLetters()

def play( message ):

    for word in message.split( '   ' ):
        playWord( word )
        playBetweenWords()


# OK, it's my turn now
play( message )



# (Wait for applauses)
stream.stop_stream()
stream.close()
player.terminate()
