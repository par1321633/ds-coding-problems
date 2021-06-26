"""
https://leetcode.com/problems/insert-interval
Medium

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            last_min, last_max = out[-1]
            if left <= last_max <= right:
                right = max(right, last_max)
                out[-1][1] = right
            elif last_max < left:
                out.append(intervals[i])
        print(out)
        return out

intervals = [[1,5]]
newInterval = [2,7]
print ("Input : intervals {}, newInterval {}".format(intervals, newInterval))
ans = Solution().insert(intervals, newInterval)
print ("Solution : {}".format(ans))

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print("Input : intervals {}, newInterval {}".format(intervals, newInterval))
ans = Solution().insert(intervals, newInterval)
print("Solution : {}".format(ans))


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print("Input : intervals {}, newInterval {}".format(intervals, newInterval))
ans = Solution().insert(intervals, newInterval)
print("Solution : {}".format(ans))