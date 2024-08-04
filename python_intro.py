from math import pow, pi

address_dict = {
    'Lev': 'Ostrovskogo'
}

def find2(name):
    return address_dict[name]


class Figure:
    def square(self):
        pass


class Square(Figure):
    def __init__(self, x) -> None:
        self.x = x

    def square(self):
        return self.x * self.x


class Circle(Figure):
    def __init__(self, r) -> None:
        self.r = r

    def square(self):
        return pi * pow(self.r, 2)


def print_square(figures: list[Figure]):
    print('it works!')
    for f in figures:
        print(f.square())

print_square([Square(10), Square(20), Circle(5), Figure()])