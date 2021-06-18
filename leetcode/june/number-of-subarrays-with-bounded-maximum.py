"""
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input:
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


Sliding Window Method

"""
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # print (nums)
        # print (left, right)
        dp = [0] * len(nums)
        k = 0

        start = -1
        end = -1

        max_index = 0

        for i in range(len(nums)):
            # print ("===========")
            # print (i, nums[i])

            if left <= nums[i] <= right:
                end = i
                dp[i] = end - start

            elif nums[i] > right:
                start = i
                end = i

            elif nums[i] < left:
                print("CHECK")
                dp[i] = end - start

        # print (dp)
        return sum(dp)


nums = [2, 1, 4, 3]
left = 2
right = 3
print ("Input - Nums {}, Left {}, Right {}".format(nums, left, right))
ans =Solution().numSubarrayBoundedMax(nums, left, right)
print ("Solution - {}".format(ans))

nums = [2, 9, 2, 5, 6]
left = 2
right = 8
print ("Input - Nums {}, Left {}, Right {}".format(nums, left, right))
ans = Solution().numSubarrayBoundedMax(nums, left, right)
print ("Solution - {}".format(ans))

nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
left = 32
right = 69
print ("Input - Nums {}, Left {}, Right {}".format(nums, left, right))
ans = Solution().numSubarrayBoundedMax(nums, left, right)
print ("Solution - {}".format(ans))


nums = [876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
left = 658
right = 719
print ("Input - Nums {}, Left {}, Right {}".format(nums, left, right))
ans = Solution().numSubarrayBoundedMax(nums, left, right)
print ("Solution - {}".format(ans))