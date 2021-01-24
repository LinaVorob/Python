class Cell:
    def __init__(self, number):
        self.number_of_cells = int(number)

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells == 0:
            return f'У клеток одинаковое количество ячеек. Уменьшение производится не будет!'
        else:
            return Cell(abs(self.number_of_cells - other.number_of_cells))

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def make_order(self, num_of_line):
        left_cell = self.number_of_cells // num_of_line
        full_lines = '*'*num_of_line+'\n'
        return f'{full_lines*left_cell}{"*"*(self.number_of_cells-num_of_line*left_cell)}'


amoeba = Cell(12)
infusoria = Cell(5)
amo_infus_add = amoeba + infusoria
amo_infus_sub = amoeba - infusoria
amo_infus_mul = amoeba * infusoria
amo_infus_div = amoeba / infusoria
print(amo_infus_add.number_of_cells)
print(amo_infus_sub.number_of_cells)
print(amo_infus_mul.number_of_cells)
print(amo_infus_div.number_of_cells)
print(amoeba.make_order(5))
