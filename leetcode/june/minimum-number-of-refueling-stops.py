"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.


Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


"""


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        print(dp)
        for i, (location, capacity) in enumerate(stations):
            print("=================")
            print(i, location, capacity)
            for t in range(i, -1, -1):
                print(t, dp)
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
        print(dp)
        for i, d in enumerate(dp):
            if d >= target: return i
        return -1


target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
Solution().minRefuelStops(target, startFuel, stations)

target = 100
startFuel = 50
stations = [[25,25],[50,50]]
Solution().minRefuelStops(target, startFuel, stations)

target = 100
startFuel = 50
stations = [[40,50]]
Solution().minRefuelStops(target, startFuel, stations)


#target = 100, startFuel = 1, stations = [[10,100]]
target = 100
startFuel = 1
stations = [[10,100]]
Solution().minRefuelStops(target, startFuel, stations)

#target = 100, startFuel = 1, stations = [[10,100]]
target = 100
startFuel = 1
stations = []
Solution().minRefuelStops(target, startFuel, stations)

