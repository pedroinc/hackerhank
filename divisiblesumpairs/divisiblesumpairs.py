#!/bin/python3


class DivSumPairs:
    def __init__(self, n, k, ar):
        if n < 2 or n > 100:
            raise ValueError()
        if k <= 0 or k > 100:
            raise ValueError()
        self._n = n
        self._k = k
        self._ar = ar

    def get_total(self):
        count = 0
        for i in range(0, self._n):
            for j in range(i+1, self._n):
                if (self._ar[i] + self._ar[j]) % self._k == 0:
                    count += 1
        return count


if __name__ == '__main__':

    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = list(map(int, input().strip().split(' ')))

    div_sum_pairs = DivSumPairs(n, k, ar)
    print(div_sum_pairs.get_total())
