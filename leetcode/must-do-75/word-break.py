"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

"""
from typing import List



class Solution:
    def __init__(self):
        self.exist = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print(s, wordDict)

        d = set(wordDict)

        def backtrack(s):
            print(s)
            if s in d:
                self.exist = True
                return

            for i in wordDict:
                if s[:len(i)] == i:
                    backtrack(s[len(i):])

        backtrack(s)
        return self.exist

class Solution:
    def recur(self, s: str, wordDict: List[str], memo) -> bool:
        if not s:
            return True
        if s in memo.keys():
            return memo[s]

        result = False
        for word in wordDict:
            if s[:len(word)] == word:
                suffix = s[len(word):]
                memo[suffix] = self.recur(suffix, wordDict, memo)
                result = result or memo[suffix]

        return result

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.recur(s, wordDict, memo)