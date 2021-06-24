"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]


"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        print (head, left, right)
        if left >= right:
            return head
        curr = head
        val = []
        while curr:
            val.append(curr.val)
            curr = curr.next
        print (val)
        val = val[:left-1] + val[left-1:right][::-1] + val[right:]
        head2 = ListNode(0)
        curr = head2
        for i in val:
            curr.next = ListNode(i)
            curr = curr.next
        return head2.next


#head = [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
left = 2
right = 4
Solution().reverseBetween(head, left, right)