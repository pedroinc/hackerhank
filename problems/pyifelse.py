
class PyIfElse:
    # If  is odd, print Weird
    # If  is even and in the inclusive range of 2 to 5, print Not Weird
    # If  is even and in the inclusive range of 6 to 20, print Weird
    # If  is even and greater than 20, print Not Weird
    def __call__(self, number):
        if number < 1 or number > 100:
            raise ValueError()
        if number % 2 == 0:
            if number in range(2, 6):
                return "Not Weird"
            elif number in range(6, 21):
                return "Weird"
            elif number > 20:
                return "Not Weird"
        else:
            return "Weird"

if __name__ == '__main__':
    n = int(input())
    number_type = PyIfElse()
    res = number_type(n)
    print(res)
