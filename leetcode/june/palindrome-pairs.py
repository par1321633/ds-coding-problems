"""
https://leetcode.com/problems/palindrome-pairs/

Level - Hard

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

"""

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        print (words)
        res = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                val = words[i] + words[j]
                if val == val[::-1]:
                    res.append([i,j])
                val = words[j] + words[i]
                if val == val[::-1]:
                    res.append([j,i])
        return res


class Solution2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words: return [[]]
        lookup = {w: i for i,w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, suf = w[:j], w[j:]
                if pre==pre[::-1] and suf[::-1]!=w and suf[::-1] in lookup:
                    res.append([lookup[suf[::-1]], i])
                if suf==suf[::-1] and pre[::-1]!=w and pre[::-1] in lookup and j!=len(w):
                    res.append([i, lookup[pre[::-1]]])
        return res


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        perSideSum = perimeter // 4
        visited = [False][len(matchsticks)]

        def canFormSquare(k, sum, cs, nums, visited, start):
            if (k == 1):
                return True

            if (cs == sum):
                return canFormSquare(k - 1, sum, 0, nums, visited, 0)

            for i in range(len(nums)):
                if (not visited[i] and cs + nums[i] <= sum):
                    visited[i] = True
                    if (canFormSquare(k, sum, cs + nums[i], nums, visited, i + 1)):
                        return True
                visited[i] = False

            return False

        return canFormSquare(4, perSideSum, 0, matchsticks, visited, 0)


words = ["abcd","dcba","lls","s","sssll"]
print ("Input - words : {}".format(words))
ans = Solution().palindromePairs(words)
print ("Solution - {}".format(ans))

words = ["bat","tab","cat"]
print ("Input - words : {}".format(words))
ans = Solution().palindromePairs(words)
print ("Solution - {}".format(ans))

words = ["a",""]
print ("Input - words : {}".format(words))
ans = Solution().palindromePairs(words)
print ("Solution - {}".format(ans))