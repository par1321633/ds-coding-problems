"""
https://leetcode.com/problems/generate-parentheses/

Level - Medium


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        print(n)
        out = []

        def backtrack(i, j, res):
            if i == n and j == n:
                print(res)
                out.append(res)
                return

            if i < n:
                backtrack(i + 1, j, res + '(')

            if j < n and j < i:
                backtrack(i, j + 1, res + ')')

        backtrack(0, 0, '')

        return out


n = 3
print ("Input - {}".format(n))
ans = Solution().generateParenthesis(n)
print ("Solution - {}".format(ans))


n = 1
print ("Input - {}".format(n))
ans = Solution().generateParenthesis(n)
print ("Solution - {}".format(ans))

