"""
https://leetcode.com/problems/jump-game-vi/

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

"""

from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]* len(nums)
        dp[0] = nums[0]
        for i in range(1, len(dp)):
            arr = dp[i - k :i] if k < i else dp[0:i]
            print (arr)
            dp[i] = max(dp[i - k :i] if k < i else dp[0:i]) + nums[i]
        print (dp)
        return dp[-1]

nums = [10,-5,-2,4,0,3]
k = 3
Solution().maxResult(nums, k)

nums = [1,-1,-2,4,-7,3]
k = 2
Solution().maxResult(nums, k=2)