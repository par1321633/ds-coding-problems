"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

"""

import itertools
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        print(candidates)
        out = []

        def backtrack(index, target_val, res):
            if target_val == target:
                print(target_val, res)
                out.append(sorted(res))
                return

            if target_val > target:
                return

            for i in range(len(candidates)):
                res.append(candidates[i])
                backtrack(i + 1, target_val + candidates[i], res)
                res.pop()

        backtrack(0, 0, [])
        out.sort()
        return list(k for k, _ in itertools.groupby(out))


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # print (candidates)
        candidates = {val: index for index, val in enumerate(candidates)}
        out = []

        def backtrack(index, target_val, res):
            if target_val == target:
                # print (target_val, res)
                out.append(res.copy())
                return

            if target_val > target:
                return

            for i in range(index, target + 1):
                if i not in candidates:
                    continue
                res.append(i)
                backtrack(i, target_val + i, res)
                res.pop()

        backtrack(0, 0, [])

        return out


candidates = [2,3,6,7]
target = 7
print ("Input : {}".format(candidates, target))
ans = Solution2().combinationSum(candidates, target)
print ("Solution : {}".format(ans))