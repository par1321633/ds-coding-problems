"""
https://leetcode.com/problems/valid-parentheses/

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false


"""


class Solution:
    def isValid(self, s: str) -> bool:
        print(s)
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for i in s:
            print(i)
            if len(stack) > 0 and d.get(stack[-1]) == i:
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack) == 0


s = "([)]"
print ("Input : {}".format(s))
ans = Solution().isValid(s)
print ("Solution : {}".format(ans))

s = "()[]{}"
print ("Input : {}".format(s))
ans = Solution().isValid(s)
print ("Solution : {}".format(ans))