#!/bin/python3

import sys


def solve(grades):

    new_grades = []

    for g in grades:
        counter = 1
        g_increased = False
        while counter < 3:
            if (g + counter) % 5 == 0 and g + counter >= 40:
                new_grades.append(g + counter)
                g_increased = True
                break

            counter += 1

        if not g_increased:
            new_grades.append(g)

    return new_grades


n = int(input().strip())
grades = []
grades_i = 0

for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))

