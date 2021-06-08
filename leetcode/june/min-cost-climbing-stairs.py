"""
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        print(cost)
        if len(cost) == 0:
            return 0
        if len(cost) < 2:
            return min(cost)
        dp = [None] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            print(cost[i])
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])
        print(dp)
        return min(dp[-2:])
