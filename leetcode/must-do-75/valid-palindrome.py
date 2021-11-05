"""
Easy
https://leetcode.com/problems/valid-palindrome/

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        haRegex = re.compile(r'[a-z0-9]')
        start = 0
        end = len(s) - 1
        while start <= end:
            if not haRegex.search(s[start]):
                start = start + 1
                continue

            if not haRegex.search(s[end]):
                end = end - 1
                continue

            if s[start] == s[end]:
                start = start + 1
                end = end - 1
            else:
                return False
        return True
