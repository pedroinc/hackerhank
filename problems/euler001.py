#!/bin/python3

def sum_of_multiples(limiter):
    if limiter <= 0 or limiter > 10**9:
        raise ValueError()
    sum = 0
    for x in range(1, limiter):
        if int(x % 3) == 0 or int(x % 5) == 0:
            sum = sum + x
    return sum

if __name__ == '__main__':

    t = int(input().strip())

    if t > 10**5:
        raise ValueError()

    m_values = []
    for a0 in range(t):
        n = int(input().strip())
        m_values.append(n)

    for item in m_values:
        print(sum_of_multiples(item))
