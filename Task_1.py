class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        max_len = 1
        if len(self.matrix) != 1:
            for el in self.matrix:
                len_of_el = (max(map(len, map(str, el))))
                max_len = max(max_len, len_of_el)
        for el in range(len(self.matrix)):
            for el_of_list in range(len(self.matrix[el])):
                self.matrix[el][el_of_list] = str(self.matrix[el][el_of_list]) + ' ' * (
                        max_len - len(str(self.matrix[el][el_of_list])))
            self.matrix[el] = ' '.join(self.matrix[el])
        return '\n'.join(self.matrix)

    def __add__(self, other):
        try:
            new_matrix = []
            for el in enumerate(self.matrix):
                line_of_matrix = list(map(lambda x, y: x + y, el[1], other.matrix[el[0]]))
                new_matrix.append(line_of_matrix)
            return Matrix(new_matrix)
        except IndexError:
            return f'Ошибка! Попытка сложить матрицы с разной размерностью!'


matrix_3_2_a = Matrix([[31, 22], [123, 321], [1, 3]])
matrix_3_2_b = Matrix([[102, 222], [32, 561], [6, 9]])
matrix_2_3_a = Matrix([[12, 345, 1], [34, 23, -1]])
matrix_2_3_b = Matrix([[124, -44, 1441], [3.4, 21, 0]])
matrix_1_8 = Matrix([[1, 2, 3, 4, 5, 6, 73, 8]])
matrix_3_5 = Matrix([[567, 43, 213], [45, 111, 9.2], [34, 23, -1], [3111, 23, 11], [87, 2.3, -90]])

print(matrix_3_2_a, end='\n\n')
print(matrix_3_2_b, end='\n\n')
print(matrix_2_3_a, end='\n\n')
print(matrix_2_3_b, end='\n\n')
print(matrix_1_8, end='\n\n')
print(matrix_3_5, end='\n\n')

matrix_new = matrix_2_3_a + matrix_1_8
print(matrix_new)
