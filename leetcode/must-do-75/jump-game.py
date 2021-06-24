"""
https://leetcode.com/problems/jump-game/
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_l = 0
        for i in range(len(nums)-1):
            print (i, nums[i])
            max_l = max(max_l, i + nums[i])
            if max_l <= i and nums[i] == 0:
                return False
        print (max_l)
        return max_l >= len(nums) - 1
    

nums = [0,2,3]
print ("Input - {}".format(nums))
ans = Solution().canJump(nums)
print ("Solution - {}".format(ans))

nums = [2,0]
print ("Input - {}".format(nums))
ans = Solution().canJump(nums)
print ("Solution - {}".format(ans))

nums = [0]
print ("Input - {}".format(nums))
ans = Solution().canJump(nums)
print ("Solution - {}".format(ans))

nums = [3,2,1,0,4]
print ("Input - {}".format(nums))
ans = Solution().canJump(nums)
print ("Solution - {}".format(ans))