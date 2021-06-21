"""
https://leetcode.com/problems/pascals-triangle/

Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        print(numRows)
        dp = []

        for i in range(0, numRows):
            arr = [None] * (i + 1)
            print(arr, dp)
            arr[0] = 1
            arr[-1] = 1
            for j in range(1, i):
                arr[j] = dp[i - 1][j] + dp[i - 1][j - 1]
            dp.append(arr)
        print(dp)
        return dp


numRows = 5
ans = Solution().generate(5)
print ("Solution : {}".format(ans))