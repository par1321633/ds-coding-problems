"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        print(preorder, inorder)

        def create_tree(preorder, inorder):
            if len(preorder) == 0:
                return None
            # print ("CREATE TREE METHOD")
            # print (preorder, inorder)
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root
            index = inorder.index(preorder[0])
            ltree = inorder[:index]
            rtree = inorder[index + 1:]
            # print ("ARRAYS")
            # print (preorder[1:1+len(ltree)],
            #       preorder[1+len(ltree):])
            # print (ltree, rtree)
            root.left = create_tree(preorder[1:1 + len(ltree)], ltree)
            root.right = create_tree(preorder[1 + len(ltree):], rtree)
            return root

        sol = create_tree(preorder, inorder)
        return sol

preorder = [1,2]
inorder = [2,1]
ans = Solution().buildTree(preorder, inorder)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = Solution().buildTree(preorder, inorder)
