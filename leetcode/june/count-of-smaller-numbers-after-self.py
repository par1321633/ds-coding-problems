"""
315. Count of Smaller Numbers After Self

Hard

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
"""

from sortedcontainers import SortedList
from typing import List


class Solution:
    def countSmaller(self, nums):
        SList, ans = SortedList(), []
        for num in nums[::-1]:
            ind = SortedList.bisect_left(SList, num)
            ans.append(ind)
            SList.add(num)

        return ans[::-1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        print (nums)
        out = [0] * len(nums)
        l = []
        for i in range(len(nums)-1,-1, -1):
            l.append(nums[i])
            l.sort()
            index = l.index(nums[i])
            out[i] = index
        return out