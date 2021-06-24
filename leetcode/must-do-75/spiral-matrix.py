"""

Given an m x n matrix, return all elements of the matrix in spiral order.


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        print(matrix)
        start = 0
        vend = len(matrix[0]) - 1
        hend = len(matrix) - 1
        k = 0
        out = []
        while start <= hend:
            if vend >= start and k % 4 == 0:
                for i in range(start, vend + 1):
                    print(matrix[start][i])
                    out.append(matrix[start][i])
                k = k + 1
            if hend > start and k % 4 == 1:
                for i in range(start + 1, hend + 1):
                    out.append(matrix[i][vend])
                k = k + 1
            if vend > start and k % 4 == 2:
                for i in range(vend - 1, start - 1, -1):
                    out.append(matrix[hend][i])
                k = k + 1
            if hend >= start and k % 4 == 3:
                for i in range(hend - 1, start, -1):
                    out.append(matrix[i][start])
                k = k + 1
            start = start + 1
            vend = vend - 1
            hend = hend - 1

        return out


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        if len(matrix) == 0:
            return
        end_col = len(matrix[0]) - 1
        movement = ['R', 'D', 'L', 'U']
        out = []
        spiral_traverse_matrix(matrix, 0, start_row, start_col, end_row, end_col, out, movement)
        return out


def spiral_traverse_matrix(matrix, index, start_row, start_col, end_row, end_col, out, movement):
    print(matrix, index, start_row, start_col, end_row, end_col)
    print(start_row >= end_row)
    print(start_col >= end_col)

    if end_row < 0 or end_col < 0:
        return

    if start_row > end_row or start_col > end_col:
        return

    op = movement[index % len(movement)]
    print(op)
    if op == 'R':
        for i in range(start_col, end_col + 1):
            print(matrix[start_row][i])
            out.append(matrix[start_row][i])
        return spiral_traverse_matrix(matrix, index + 1, start_row + 1, start_col, end_row, end_col, out, movement)
    elif op == 'D':
        for i in range(start_row, end_row + 1):
            print(matrix[i][end_col])
            out.append(matrix[i][end_col])
        return spiral_traverse_matrix(matrix, index + 1, start_row, start_col, end_row, end_col - 1, out, movement)
    elif op == 'L':
        print(end_col, start_col)
        for i in range(end_col, start_col - 1, -1):
            print(matrix[end_row][i])
            out.append(matrix[end_row][i])
        return spiral_traverse_matrix(matrix, index + 1, start_row, start_col, end_row - 1, end_col, out, movement)
    elif op == 'U':
        for i in range(end_row, start_row - 1, -1):
            print(matrix[i][start_col])
            out.append(matrix[i][start_col])
        return spiral_traverse_matrix(matrix, index + 1, start_row, start_col + 1, end_row, end_col, out, movement)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print ("Input : {}".format(matrix))
ans = Solution().spiralOrder(matrix)
print ("Solution : {}".format(ans))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print ("Input : {}".format(matrix))
ans = Solution().spiralOrder(matrix)
print ("Solution : {}".format(ans))


