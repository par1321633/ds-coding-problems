"""

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        print(nums)
        nums.sort()
        print(nums)
        ans = 1
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 0:
                continue
            if nums[i] - nums[i - 1] == 1:
                diff = diff + 1
            else:
                diff = 1
            if diff > ans:
                ans = diff
            print(nums[i], nums[i - 1], ans, diff)

        return ans