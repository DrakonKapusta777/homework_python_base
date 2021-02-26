class Matrix:
    def __init__(self, list_1, list_2):
        self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return str('\n'.join(['\n'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[2, 11, 11],
                    [44, 123, 23],
                    [11, 5, 5]],
                   [[2, 2, 2],
                    [53, 54, 63],
                    [2, 211, 1]])

print(my_matrix.__str__())
print(my_matrix.__add__())
