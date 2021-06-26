"""
https://leetcode.com/problems/merge-two-sorted-lists/

Easy

Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # print (l1, l2)
        outl = ListNode(None)
        out = outl
        while l1 and l2:
            if l1.val < l2.val:
                out.next = ListNode(l1.val)
                l1 = l1.next
            else:
                out.next = ListNode(l2.val)
                l2 = l2.next
            out = out.next

        while l1:
            out.next = ListNode(l1.val)
            out = out.next
            l1 = l1.next

        while l2:
            out.next = ListNode(l2.val)
            out = out.next
            l2 = l2.next

        return outl.next


#l1 = [1,2,4]
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

#l2 = [1,3,4]
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
ans = Solution().mergeTwoLists(l1, l2)
