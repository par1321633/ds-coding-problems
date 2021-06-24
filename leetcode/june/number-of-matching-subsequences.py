"""
https://leetcode.com/problems/number-of-matching-subsequences/

Medium

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        print(s)
        n = len(s)

        def issubseq(word, string, n):
            stack = []
            for i in word:
                stack.append(i)
            for i in range(n - 1, -1, -1):
                if not stack:
                    return True
                if stack[-1] == string[i]:
                    stack.pop()
            return stack == []

        cnt = 0
        d = {}

        for i in words:
            if i not in d:
                d[i] = False
                if issubseq(i, s, n):
                    cnt = cnt + 1
                    d[i] = True
            else:
                if d[i]:
                    cnt = cnt + 1
        return cnt


s = "abcde"
words = ["a","bb","acd","ace"]
print ("Input : String {}, Words {}".format(s, words))
ans = Solution().numMatchingSubseq(s, words)
print ("Solution : {}".format(ans))