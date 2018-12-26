import struct
from random import shuffle

DICTIONARY = 'IYURO#{EW}GMFSK!LT_AH'
PATH = 'secret.gif'


def z(n):
    import math
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i


def solve_letter(letter, is_uppercase):
    if letter[0] == 1:
        ret = DICTIONARY[letter[1] >> 1].lower()
    elif letter[0] == 0 and letter[1] == 1:
        ret = DICTIONARY[letter[3] >> 2].lower()
    else:
        ret = DICTIONARY[int(letter[2] * letter[3])].lower()

    return ret.upper() if is_uppercase else ret

with open(PATH, 'rb') as f:
    buffer = f.read()

flag = ''
start = buffer.find(b'\x21\xf9\x04\x05\x03')
while start > -1:
    chunk = buffer[start:start + 17]
    letter = struct.unpack('<HHHH', chunk[9:])

    flag += solve_letter(letter, chunk[6] % 2 == 1)

    buffer = buffer[start + 17:]
    start = buffer.find(b'\x21\xf9\x04\x05\x03')

print(flag)
