"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

"""

from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # print (root)
        def get_length_of_tree(root, l):
            if root is None:
                return l
            return max(get_length_of_tree(root.left, l + 1),
                       get_length_of_tree(root.right, l + 1))

        l = get_length_of_tree(root, 0)
        # print (l)
        out = [[] for i in range(l)]

        def in_order_traversal(root, l):
            if root is None:
                return
            out[l].append(root.val)
            in_order_traversal(root.left, l + 1)
            in_order_traversal(root.right, l + 1)
        in_order_traversal(root, 0)
        return out