#!/bin/python3

import sys, math, itertools


def bigger_is_greater(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_values = []

    for letter in word:
        letter_values.append(alphabet.find(letter))

    if len(word) == 1:
        return "no answer"

    if all(x == letter_values[0] for x in letter_values):
        return "no answer"

    m_suffix_indexes = []
    m_suffix_value = []
    last_value = -1

    #find longest non-increasing suffix
    for i in range(len(letter_values) - 1, -1, -1):
        if letter_values[i] >= last_value:
            m_suffix_indexes.append(letter_values[i])
            # m_suffix_value.append()
            last_value = letter_values[i]
        else:
            break

    m_suffix_indexes.reverse()

    # identify pivot
    length_letter_values = len(letter_values)
    length_suffix = len(m_suffix_indexes)
    pivot_index = (length_letter_values - 1) - length_suffix
    pivot_value = letter_values[pivot_index]

    rightmost_sucessor_idx = -1
    rightmost_sucessor_val = -1

    #find rightmost sucessor to pivot in the suffix
    for i in range(len(m_suffix_indexes) - 1, -1, -1):
        if m_suffix_indexes[i] >= pivot_value:
            rightmost_sucessor_val = m_suffix_indexes[i]
            #last_occur_of_value
            rightmost_sucessor_idx = (len(letter_values) - 1) - letter_values[::-1].index(rightmost_sucessor_val)

    #swap the pivot


    #reverse the suffix


    # m_suffix_indexes.append(letter_values[i])
    # m_suffix_value.append(alphabet[letter_values[i]])
    # return m_suffix_indexes, m_suffix_value

    return m_suffix_indexes, letter_values, pivot_value, letter_values.index(rightmost_sucessor_val)


if __name__ == "__main__":

    words = []
    new_words = []
    n = int(input().strip())

    for a0 in range(n):
        words.append(input().strip())

    for w in words:
        result = bigger_is_greater(w)
        new_words.append(result)

    for nw in new_words:
        print(nw)
