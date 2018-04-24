# https://stackoverflow.com/questions/31412252/my-code-is-inefficent-multiples-of-3-and-5-from-project-euler-but-with-a-10-sec
# https://stackoverflow.com/users/216074/poke

def euler1 (n):
    max3 = range(0, n, 3)[-1]
    max5 = range(0, n, 5)[-1]
    max15 = range(0, n, 15)[-1]

    sum3 = (max3 + 3) * max3 // 3 // 2
    sum5 = (max5 + 5) * max5 // 5 // 2
    sum15 = (max15 + 15) * max15 // 15 // 2

    return sum3 + sum5 - sum15
