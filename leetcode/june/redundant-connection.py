"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


 Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

"""
from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print(edges)
        d = defaultdict(list)

        def dfs(u, v):
            if u not in visied:
                visied.append(u)
                if u == v: return True
                return any(dfs(nei, v) for nei in d[u])

        for i in edges:
            u, v = i
            visied = []
            if u in d and v in d and dfs(u, v):
                return i
            d[u].append(v)
            d[v].append(u)


edges = [[1,2],[1,3],[2,3]]
print ("Input : {}".format(edges))
ans =Solution().findRedundantConnection(edges)
print ("Solution : {}".format(ans))


edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print ("Input : {}".format(edges))
ans = Solution().findRedundantConnection(edges)
print ("Solution : {}".format(ans))
