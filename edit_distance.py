# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 20:56


def levenshtein_distance(str1, str2):
    m, n = len(str1) + 1, len(str2) + 1

    # 初始化矩阵
    matrix = [[0] * n for i in range(m)]
    matrix[0][0] = 0

    for i in range(1, m):
        matrix[i][0] = matrix[i - 1][0] + 1
    for j in range(1, n):
        matrix[0][j] = matrix[0][j - 1] + 1

    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i-1][j]+1, matrix[i][j-1]+1)
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1]+1, matrix[i - 1][j]+1, matrix[i][j - 1]+1)

    return matrix[m - 1][n - 1]


if __name__ == '__main__':
    str1 = "abcd"
    str2 = "abc"
    print(levenshtein_distance(str1, str2))