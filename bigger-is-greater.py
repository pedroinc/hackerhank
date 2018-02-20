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

    possible_anagrams = ["".join(perm) for perm in itertools.permutations(word)]

    # sort the anagrams
    ordered_anagrams = sorted(possible_anagrams)

    # retrieve the anagram's index immediate bigger than the
    start_position = ordered_anagrams.index(word)
    new_position = start_position + 1

    while True:
        try:
            if ordered_anagrams[new_position] > ordered_anagrams[start_position]:
                break
            else:
                new_position = new_position + 1
        except IndexError:
            return "no answer"

    # return the anagram
    return ordered_anagrams[new_position]


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
