""""
https://leetcode.com/problems/maximum-units-on-a-truck/

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.


Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

"""

from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        print (boxTypes, truckSize)
        d = {}
        for key,val in boxTypes:
            d[val] = d.get(val,0) + key
        print (d)
        ans = 0
        for w in sorted(d,reverse=True):
            print (w, d[w], ans, truckSize)
            if truckSize < 0:
                break
            val = d[w] if truckSize > d[w] else truckSize
            ans = ans + (w * val)
            truckSize = truckSize - d[w]
        return ans


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print ("Input - Box Types : {}, Truck Size : {}".format(boxTypes, truckSize))
ans = Solution().maximumUnits(boxTypes, truckSize)
print ("Solution - {}".format(ans))


boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize  = 10
print ("Input - Box Types : {}, Truck Size : {}".format(boxTypes, truckSize))
ans = Solution().maximumUnits(boxTypes, truckSize)
print ("Solution - {}".format(ans))


boxTypes = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]
truckSize = 13
print ("Input - Box Types : {}, Truck Size : {}".format(boxTypes, truckSize))
ans = Solution().maximumUnits(boxTypes, truckSize)
print ("Solution - {}".format(ans))