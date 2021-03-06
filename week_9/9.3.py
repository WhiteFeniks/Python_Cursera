import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def __str__(self):
        my_str = self.lst
        i = 0
        res = ""
        while i < len(my_str):
            j = 0
            while j < len(my_str[i]):
                if j + 1 == len(my_str[i]):
                    res = res + str(my_str[i][j])
                    break
                res = res + str(my_str[i][j]) + '\t'
                j += 1
            res = res + '\n'
            i += 1
        res = res[0:-1]
        return res

    def size(self):
        first = len(self.lst)
        second = len(self.lst[0])
        k = tuple([first, second])
        return k

    def __add__(self, other):
        if not len(self.lst) == len(other.lst):
            raise MatrixError(self, other)
        res = []
        i = 0
        while i < len(self.lst):
            j = 0
            temp = []
            while j < len(self.lst[i]):
                x = self.lst[i][j] + other.lst[i][j]
                temp.append(x)
                j += 1
            res.append(temp)
            i += 1
        return Matrix(res)

    def __mul__(self, other):
        res = []
        i = 0
        while i < len(self.lst):
            j = 0
            temp = []
            while j < len(self.lst[i]):
                x = self.lst[i][j] * other
                temp.append(x)
                j += 1
            res.append(temp)
            i += 1
        return Matrix(res)
    __rmul__ = __mul__

    def transpose(self):
        new_matrix = list(zip(*self.lst))
        self.lst = new_matrix
        return Matrix(new_matrix)

    def transposed(self):
        new_matrix = list(zip(*self.lst))
        return Matrix(new_matrix)


exec(stdin.read())
