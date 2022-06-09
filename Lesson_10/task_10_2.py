from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):
    reserve_cloth = 0

    def __init__(self, size):
        self.size = size

    @property
    def expense(self):
        return self.size/6.5 + 0.5

    @property
    def add_to_reserve(self):
        Coat.reserve_cloth += self.expense

    def show_reserve(self):
        return self.reserve_cloth

class Suit(Clothes):
    reserve_cloth = 0

    def __init__(self, height):
        self.height = height

    @property
    def expense(self):
        return self.height*2 + 0.3

    @property
    def add_to_reserve(self):
        Suit.reserve_cloth += self.expense

    def show_reserve(self):
        return self.reserve_cloth

# a = Coat(52)
# b = Suit(1.80)
# print(a)
# print(a.expense)
# print(b.expense)


c1 = Coat(12)
c2 = Coat(1)
c3 = Coat(121)
c4 = Coat(23)
c1.add_to_reserve
c2.add_to_reserve
print(c1.expense)
print(c2.expense)
print(Coat.reserve_cloth)

s1 = Suit(12)
s2 = Suit(1)
s3 = Suit(121)
s4 = Suit(23)
s1.add_to_reserve
s2.add_to_reserve
print(s1.expense)
print(s2.expense)
print(Suit.reserve_cloth)