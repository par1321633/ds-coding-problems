"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


1047. Remove All Adjacent Duplicates In String


You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        print(s)
        start = 0
        end = len(s)

        while start < end - 1:
            if s[start] == s[start + 1]:
                s = s[:start] + s[start + 2:]
                end = end - 2
                start = start - 1 if start > 1 else 0
            else:
                start = start + 1
        if end == 0:
            return ''
        return s

class Solution2:
    def removeDuplicates(self, s):
        stack = []
        for symb in s:
            if stack and stack[-1] == symb:
                stack.pop()
            else:
                stack.append(symb)
        return "".join(stack)


s = "aaaaaaaaa"
print ("Input - s: {}".format(s))
ans = Solution().removeDuplicates(s)
print ("Solution : {}".format(ans))


s = "abbaca"
print ("Input - s: {}".format(s))
ans = Solution().removeDuplicates(s)
print ("Solution : {}".format(ans))


s = "azxxzy"
print ("Input - s: {}".format(s))
ans = Solution().removeDuplicates(s)
print ("Solution : {}".format(ans))
