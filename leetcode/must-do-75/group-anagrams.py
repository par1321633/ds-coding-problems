"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]

"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print (strs)
        anagram_hash = {}
        #ans = []
        for i in strs:
            res = ''.join(sorted(i))
            anagram_hash[res] = anagram_hash.get(res,[]) + [i]
        print (anagram_hash)
        #for i in anagram_hash:
        #    ans.append(anagram_hash.get(i))
        return anagram_hash.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print ("Input - Strings: {}".format(strs))
ans = Solution().groupAnagrams(strs)
print ("Solution - {}",format(ans))