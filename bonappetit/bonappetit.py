#!/bin/python3


class BonAppetit:
    def __init__(self, num_items, wont_eat, items, charge_price):
        if wont_eat >= len(items):
            raise IndexError()

        self._num_items = num_items
        self._wont_eat = wont_eat
        self._items = items
        self._charge_price = charge_price

    def calculate_annas_bill(self):
        bill_without_item = 0
        for i in range(0, self._num_items):
            if i != self._wont_eat:
                bill_without_item = bill_without_item + self._items[i]
        return bill_without_item / 2

    def get_answer(self):
        annas_bill = self.calculate_annas_bill()
        if annas_bill == self._charge_price:
            return 'Bon Appetit'
        else:
            return int(self._charge_price - annas_bill)

if __name__ == '__main__':

    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    bill = list(map(int, input().strip().split(' ')))
    b = int(input())

    bonappetit = BonAppetit(n, k, bill, b)
    print(bonappetit.get_answer())
