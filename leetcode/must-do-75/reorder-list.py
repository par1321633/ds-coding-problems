"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = []
        hcopy = head
        while hcopy:
            vals.append(hcopy.val)
            hcopy = hcopy.next

        if len(vals) != 1:
            l = 0
            r = len(vals) - 1
            while l < r:
                head.val = vals[l]
                head.next.val = vals[r]
                l += 1
                r -= 1
                head = head.next.next

            if l == r and head is not None:
                head.val = vals[l]
