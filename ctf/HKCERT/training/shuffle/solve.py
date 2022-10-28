# Writeup from https://ankmak.com/tech/2021/11/21/HK-Cyber-Security-New-Generation-CTF-Challenge-2021.html

import random

output = b'p\xbcl\xf0Y3C#\xf5\xf8\xb0\xe6\x98%\x17\xaf\xa8\x1d\xf1\x19\xb3i\x9aj\x1e\xccx\xb7F\xea\xfa]\r\xf1X\xc1\x8e\xee'
flag = b''
random.seed(len(output))

for c in output:
    res = list(map(int, bin(c)[2:].rjust(8, '0')))
    my_list = list(range(8))
    random.shuffle(my_list)

    ans_res = [0] * 8
    j = 0

    for i in my_list:
        ans_res[i] = res[j]
        j += 1

    shuffled = int(''.join(map(str, ans_res)), 2)
    flag += bytes([shuffled])

print(flag)