"""
https://leetcode.com/problems/set-matrix-zeroes/

Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        def process(i, j):
            for k in range(len(matrix[i])):
                matrix[i][k] = 0

            for k in range(len(matrix)):
                # print (matrix[k][j])
                matrix[k][j] = 0

        for i in queue:
            process(i[0], i[1])
        print(matrix)


class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print ("Input : {}".format(matrix))
ans = Solution().setZeroes(matrix)
print ("Solution : {}".format(ans))

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print ("Input : {}".format(matrix))
ans = Solution().setZeroes(matrix)
print ("Solution : {}".format(ans))