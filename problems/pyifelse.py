
class PyIfElse:
    def __init__(self, number):
        self._number = number

    def __call__(self):
        if self._number % 2 != 0:
            print("Weird")

if __name__ == '__main__':
    # n = int(input())

    x = PyIfElse(5)
    x()
