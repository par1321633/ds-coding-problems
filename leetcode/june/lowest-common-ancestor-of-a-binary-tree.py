"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def searchTree(root, p, out):
            # print ("R", root.val, p, out)
            if root is None:
                return False
            if root == p:
                return out + [p.val]
            return searchTree(root.left, p, out + [root.val]) or searchTree(root.right, p, out + [root.val])

        p_out = searchTree(root, p, out=[])
        q_out = searchTree(root, q, out=[])
        # print (p_out, q_out)
        val = 0
        for i, v in zip(p_out, q_out):
            if i != v:
                break
            val = val + 1
        # print (val)
        return TreeNode(p_out[val - 1])


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left != None: return left
        return right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4))

Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(4))

Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1))

