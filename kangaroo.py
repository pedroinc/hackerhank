#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):

    default_pos = 0
    kang1_pos = x1
    kang2_pos = x2
    kang1_jump = v1
    kang2_jump = v2

    while default_pos < 100000:
        kang1_pos = kang1_pos + kang1_jump
        kang2_pos = kang2_pos + kang2_jump

        if kang1_pos == kang2_pos:
            return True

        default_pos = default_pos + 1

    return False


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
if result:
    print('YES')
else:
    print('NO')
