"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        print(nums, k)
        index_zeros = []
        val = max_val = 0
        for index, value in enumerate(nums):
            # print (val, index, index_zeros, max_val)
            if value == 0:
                index_zeros.append(index)
                if len(index_zeros) - k > 0:
                    # print ("POPED", val,  index_zeros)
                    v = index_zeros[len(index_zeros) - 1 - k]
                    val = index - v - 1
                    # print ("val", val, v)
            val = val + 1

            if val > max_val:
                max_val = val
        # print (index_zeros)
        return max_val


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print ("Input - nuns : {}, k : {}".format(nums, k))
ans = Solution().longestOnes(nums, k)
print ("Solution : {}".format(ans))


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print("Input - nuns : {}, k : {}".format(nums, k))
ans = Solution().longestOnes(nums, k)
print("Solution : {}".format(ans))


nums = [0,0,0,1]
k = 4
print ("Input - nuns : {}, k : {}".format(nums, k))
ans = Solution().longestOnes(nums, k)
print ("Solution : {}".format(ans))


nums = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
k = 8
print ("Input - nuns : {}, k : {}".format(nums, k))
ans = Solution().longestOnes(nums, k)
print ("Solution : {}".format(ans))


nums = [1,1,1,0,0,0,1,1,1,1]
k = 0
print ("Input - nuns : {}, k : {}".format(nums, k))
ans = Solution().longestOnes(nums, k)
print ("Solution : {}".format(ans))
