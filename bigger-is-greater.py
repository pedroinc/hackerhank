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

    m_suffix_index = []
    m_suffix_value = []
    last_value = -1

    #find longest non-increasing suffix
    for i in range(len(letter_values) - 1, -1, -1):
        if letter_values[i] > last_value:
            m_suffix_index.append(letter_values[i])
            last_value = letter_values[i]
        else:
            break

    m_suffix_index.reverse()

    # m_suffix_index.append(letter_values[i])
    # m_suffix_value.append(alphabet[letter_values[i]])

    # return m_suffix_index, m_suffix_value
    return m_suffix_index, letter_values

    #identify pivot

    #find rightmost sucessor to pivot in the suffix

    #swap the pivot

    #reverse the suffix


    # possible_anagrams = ["".join(perm) for perm in itertools.permutations(word)]
    #
    # # sort the anagrams
    # ordered_anagrams = sorted(possible_anagrams)
    #
    # # retrieve the anagram's index immediate bigger than the
    # start_position = ordered_anagrams.index(word)
    # new_position = start_position + 1
    #
    # # return the anagram
    # return ordered_anagrams[new_position]


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
