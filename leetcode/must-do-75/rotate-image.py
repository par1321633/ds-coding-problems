"""
https://leetcode.com/problems/rotate-image/

Medium

Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

"""

from typing import List
import math


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        l = len(matrix)
        for i in range(l):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        z = math.ceil(l / 2)
        for i in range(z):
            for j in range(len(matrix)):
                matrix[j][i], matrix[j][l - 1 - i] = matrix[j][l - 1 - i], matrix[j][i]

        return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = Solution().rotate(matrix)