#!/bin/python3

import sys, itertools

def nonDivisibleSubset(k, all_itens):

    m_subset = []
    second_chance_list = []

    for current_value in all_itens:

        valid_number = False
        copy_of_itens = all_itens[:]
        copy_of_itens.remove(current_value)

        for xc in copy_of_itens:
            if (current_value + xc) % k != 0:
                valid_number = True
            else:
                valid_number = False

        if valid_number:
            m_subset.insert(0, current_value)
        else:
            second_chance_list.insert(0, current_value)

    #go through once more
    for chance_item in second_chance_list:
        valid_number = False

        for item in m_subset:
            if (item + chance_item) % k != 0:
                valid_number = True
            else:
                valid_number = False

        if valid_number:
            m_subset.insert(len(m_subset), current_value)

    return len(set(m_subset))


if __name__ == "__main__":

    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))

    if len(arr) != len(set(arr)):
        raise ValueError('list of itens not unique')

    result = nonDivisibleSubset(k, arr)

    print(result)
