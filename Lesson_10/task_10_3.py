class Cell:
    def __init__(self, quantity):
        self._quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'Результат операции {self._quantity * "*"}'

    def __add__(self, other):
        if isinstance(other, Cell):
        # self.result = Cell(self.quantity + other.quantity)
            return Cell(self._quantity + other._quantity)

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self._quantity > other._quantity:
                return Cell(self._quantity - other._quantity)

            raise ValueError(f"{self._quantity} - {other._quantity}: impossible operation")
        # print(f"{self._quantity} - {other._quantity}: impossible operation")

    def __mul__(self, other):
        if isinstance(other, Cell):
        # self.result = Cell(int(self.quantity * other.quantity))
            return Cell(int(self._quantity * other.quantity))

    def __truediv__(self, other):
        if isinstance(other, Cell):
        # self.result = Cell(round(self.quantity // other.quantity))
            return Cell(round(self._quantity // other._quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self._quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self._quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(43)
print(cells1)
print(cells2)
print(cells1 + cells2)
print(type(cells1 + cells2))
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)