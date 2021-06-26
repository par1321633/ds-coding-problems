"""
https://leetcode.com/problems/unique-paths/
Unique Paths

Medium
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        print(m, n)
        dp = [[None for i in range(n)] for i in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1 or i == m - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        return dp[0][0]


m = 3
n = 2
print ("Input - m : {}, n : {}".format(m, n))
ans = Solution().uniquePaths(m,n)
print ("Solution - {}".format(m,n))


m = 3
n = 7
print ("Input - m : {}, n : {}".format(m, n))
ans = Solution().uniquePaths(m,n)
print ("Solution - {}".format(m,n))