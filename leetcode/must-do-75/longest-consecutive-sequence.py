"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        z = set(nums)
        ans = 0
        for i in z:
            print("List. : {}".format(i))
            if i - 1 not in z:
                k = i
                current_streak = 1
                while k + 1 in z:
                    current_streak = current_streak + 1
                    k = k + 1

                ans = max(ans, current_streak)
        return ans