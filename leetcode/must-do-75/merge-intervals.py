"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Medium

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        out = [intervals[0]]
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            last_min, last_max = out[-1]
            # print (left,last_max, right)
            if left <= last_max <= right or left <= last_min <= right:
                left = min(left, last_min)
                right = max(right, last_max)
                out[-1] = [left, right]
            elif last_max < left:
                out.append(intervals[i])
            elif last_min > left:
                out = out[:-1] + [intervals[i]] + [out[-1]]
        print(out)
        return out


intervals =[[2,3],[4,5],[6,7],[8,9],[1,10]]
print ("Input : {}".format(intervals))
ans = Solution().merge(intervals)
print ("Solution : {}".format(ans))

intervals = [[1,4],[0,0]]
print ("Input : {}".format(intervals))
ans = Solution().merge(intervals)
print ("Solution : {}".format(ans))


intervals = [[1,4],[0,1]]
print ("Input : {}".format(intervals))
ans = Solution().merge(intervals)
print ("Solution : {}".format(ans))


intervals = [[1,3],[2,6],[8,10],[15,18]]
print ("Input : {}".format(intervals))
ans = Solution().merge(intervals)
print ("Solution : {}".format(ans))

intervals = [[1,4],[4,5]]
print ("Input : {}".format(intervals))
ans = Solution().merge(intervals)
print ("Solution : {}".format(ans))