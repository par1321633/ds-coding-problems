"""
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index: int, val: int) -> None:
        if val >= self.nums[index]:
            self.sums += (val - self.nums[index])
        else:
            self.sums -= (self.nums[index] - val)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        left_sum = sum(self.nums[:left])
        right_sum = sum(self.nums[right + 1:])
        return self.sums - left_sum - right_sum


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
param_2 = obj.sumRange(0,2)
print (param_2)
index = 1
val = 2
obj.update(index,val)
param_2 = obj.sumRange(0,2)
print (param_2)