

def capitalize(word_array):
    if len(word_array) < 0 or len(word_array) >= 1000:
        raise ValueError()

    capitalized = ""
    for word in word_array:
        if not word.isalnum():
            raise ValueError()

        first_letter = word[0].upper()
        all_the_rest = word[1:]
        capitalized = "{0}{1}{2} ".format(capitalized, first_letter, all_the_rest)

    return capitalized

if __name__ == '__main__':
    word_array = input().split()
    res = capitalize(word_array)
    print(res)
