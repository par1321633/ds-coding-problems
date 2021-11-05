"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        print (nums)
        if len(nums) == 1:
            return nums[0]

        def backtrack(start, end):
            if start == end:
                return nums[start]
            mid = (start + end) // 2
            print(nums[start], nums[end], nums[mid])
            if nums[mid] > nums[end] or nums[start] > nums[mid]:
                x = backtrack(start, mid)
                y = backtrack(mid + 1, end)
                print(x, y)
                return min(x, y)

            else:
                return nums[start]
            # print(nums[start], nums[end], nums[mid], target)

        return backtrack(0, len(nums) - 1)

