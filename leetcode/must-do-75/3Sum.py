"""
https://leetcode.com/problems/3sum/


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
from collections import Counter
from typing import List


#HASHMAP Using Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = list(counter.keys())

        ans = set()
        print(counter, nums)
        if counter[0] >= 3: ans.add((0, 0, 0))
        pos, neg = [x for x in nums if x > 0], [x for x in nums if x < 0]

        for a in neg:
            for b in pos:
                c = -(a + b)
                print(c)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    ans.add(tuple(sorted([a, b, c])))
        return ans


class DfsSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a simple dfs is enough
        l = len(nums)
        if l < 3: return []

        ans = []
        def dfs(nums, cur, pos, target, d):
            if d == 3:
                if target == 0:
                    ans.append(cur.copy())
                return

            for i in range(pos, l):
                cur.append(nums[i])
                dfs(nums, cur, i+1, target-nums[i], d+1)
                cur.pop()

        dfs(nums, [], 0, 0, 0) # nums, cur, pos, depth
        ans = set([tuple(sorted(x)) for x in ans])
        return ans


nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)
#Output: [[-1,-1,2],[-1,0,1]]