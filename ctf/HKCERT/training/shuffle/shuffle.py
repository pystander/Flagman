# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: shuffle.py
# Compiled at: 2021-08-17 20:58:36
# Size of source mod 2**32: 281 bytes
import random
flag = open('flag.txt').read().encode()
random.seed(len(flag))
output = b''
for c in flag:
    res = list(map(int, bin(c)[2:].rjust(8, '0')))
    random.shuffle(res)
    shuffled = int(''.join(map(str, res)), 2)
    output += bytes([shuffled])
else:
    print(output)
# okay decompiling shuffle.pyc
