from lib import CheckIsMatrix, MatrixIsEqual


class Matrix:
    def __init__(self, matrix_list):
        # Выполним проверку что к нам пришла верная матрица
        CheckIsMatrix(matrix_list)

        self.matrix = matrix_list

    def __str__(self):
        retstr = ""
        for i in range(0, len(self.matrix)):
            retstr = retstr + str(self.matrix[i]) + ("" if (i + 1) == len(self.matrix) else "\n")

        return retstr

    def __add__(self, other):
        #1 проверим что второе это матрица
        CheckIsMatrix(other)
        #Проверим что они эквивалентны
        MatrixIsEqual(self.matrix, other)
        # Мы ранее проверяли что матрицы соответствуют друг другу
        # Теперь цикл в цикле обходим их

        for ind_x in range(0, len(self.matrix)):
            for ind_y in range(0, len(self.matrix[ind_x])):
                self.matrix[ind_x][ind_y] = self.matrix[ind_x][ind_y] + other[ind_x][ind_y]


a_matrix = [[5, 15, 44], [15, 4, 2], [3, 15, 3]]
b_matrix = [[9, 2, 3], [14, 1, 9], [12, 1, 99]]
a = (Matrix(a_matrix))
a+b_matrix

print(a)
