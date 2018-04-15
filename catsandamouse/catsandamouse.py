import os
import sys

class CatsAndMouse:

    msg_cat_a = 'Cat A'
    msg_cat_b = 'Cat B'
    msg_mouse_c = 'Mouse C'

    def __init__(self, **kwargs):
        try:
            self.cat_a = kwargs['cat_a']
            self.cat_b = kwargs['cat_b']
            self.mouse_c = kwargs['mouse_c']

            if self.cat_a <= 0 or self.cat_a > 100:
                raise ValueError()
            if self.cat_b <= 0 or self.cat_b > 100:
                raise ValueError()
            if self.mouse_c <= 0 or self.mouse_c > 100:
                raise ValueError()

        except IndexError as ie:
            print('index not defined!')

    def get_answer(self):
        cat_a_distance_from_mouse = abs(self.cat_a - self.mouse_c)
        cat_b_distance_from_mouse = abs(self.cat_b - self.mouse_c)

        if self.cat_a == self.cat_b or cat_a_distance_from_mouse == cat_b_distance_from_mouse:
            return self.msg_mouse_c
        if cat_a_distance_from_mouse < cat_b_distance_from_mouse:
            return self.msg_cat_a
        if cat_a_distance_from_mouse > cat_b_distance_from_mouse:
            return self.msg_cat_b

if __name__ == '__main__':
    q = int(input())
    results = []
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        cats_and_mouse = CatsAndMouse(cat_a=x, cat_b=y, mouse_c=z)
        results.append(cats_and_mouse.get_answer())
    for x in results:
        print(x)
