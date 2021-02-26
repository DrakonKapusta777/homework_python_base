class Textil:
    def __init__(self, width, height):
        self.W = width
        self.H = height

    def get_square_coat(self):
        return self.W / 6.5 + 0.5

    def get_square_suit(self):
        return self.H * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.W / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.W / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_coat())
print(jacket.get_square_suit())
