"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #print (nums)
        ans = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            #print (max_sum, i)
            max_sum = max_sum + i if i < max_sum + i else i
            ans  = max_sum if max_sum > ans else ans
            #print (max_sum, ans)
            #print ("=====")
        return ans


nums = [1,2]
print ("Inpur - Nums {}".format(nums))
ans = Solution().maxSubArray(nums)
print ("Solution - {}".format(ans))

nums = [-2,-1]
print ("Inpur - Nums {}".format(nums))
ans = Solution().maxSubArray(nums)
print ("Solution - {}".format(ans))

nums = [-2,1,-3,4,-1,2,1,-5,4]
print ("Inpur - Nums {}".format(nums))
ans = Solution().maxSubArray(nums)
print ("Solution - {}".format(ans))
