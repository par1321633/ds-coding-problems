"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


 Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 0:
            return 0

        ans = hi = lo = nums[0]
        for i in range(1, len(nums)):
            hi, lo = max(hi * nums[i], lo * nums[i], nums[i]), min(hi * nums[i], lo * nums[i], nums[i])
            ans = max(ans, hi)
        return ans


nums = [2,3,-2,4]
Solution().maxProduct(nums)


nums = [-2,0,-1]
Solution().maxProduct(nums)
