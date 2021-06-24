"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        start = 0
        end = len(nums) - 1

        def backtrack(start, end):

            if start > end:
                return -1
            mid = (start + end) // 2
            print(start, end, mid)
            print(nums[start], nums[end], nums[mid])

            if nums[mid] == target:
                return mid
            if nums[mid] > nums[end] or nums[start] > nums[mid]:
                return max(backtrack(start, mid), backtrack(mid + 1, end))
            elif nums[mid] > target and nums[end]:
                return backtrack(start, mid - 1)
            elif nums[mid] < target:
                return backtrack(mid + 1, end)

        return backtrack(start, end)



