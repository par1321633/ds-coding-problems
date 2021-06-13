"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        max_count = 0
        visited = []
        for i in s:
            # print (visited, max_count)
            # print (i)
            if i in visited:
                index = visited.index(i)
                visited = visited[index + 1:]

            visited.append(i)
            if len(visited) > max_count:
                # print (visited)
                max_count = len(visited)
        return max_count


s = "aab"
Solution().lengthOfLongestSubstring(s)

s = "abcabcbb"
Solution().lengthOfLongestSubstring(s)

s = "bbbbb"
Solution().lengthOfLongestSubstring(s)

s = "pwwkew"
Solution().lengthOfLongestSubstring(s)
