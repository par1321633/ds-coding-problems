"""
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        print (nums)
        a = b = 0
        for i in range(len(nums)):
            if i%2 == 0:
                a = a + nums[i]
                a = max(a, b)
            else:
                b = b + nums[i]
                b = max(a,b)
        #print (a,b)
        return max(a,b)


nums = [1,2,3,1]
ans = Solution().rob(nums)
print(ans)

nums = [2,7,9,3,1]
ans = Solution().rob(nums)
print(ans)