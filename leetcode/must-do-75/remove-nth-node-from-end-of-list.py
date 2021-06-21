"""

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Medium


Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        print(head)

        def get_len_llist(head):
            curr = head
            cnt = 0
            while curr:
                curr = curr.next
                cnt = cnt + 1
            return cnt

        len_ll = get_len_llist(head)

        cnt = len_ll - n + 1
        # print (len_ll, cnt)

        if cnt < 1:
            return
        elif cnt == 1:
            head = head.next
            return head

        curr = head
        cnt = cnt - 1
        while curr and cnt > 1:
            curr = curr.next
            cnt = cnt - 1
        curr.next = curr.next.next
        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        print(head)
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        l = l[::-1]
        l = l[:n - 1] + l[n:]
        l = l[::-1]
        print(l)

        if len(l) == 0:
            return
        head = ListNode(l[0])
        curr = head
        for i in range(1, len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next
        return head


#head = [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
ans = Solution().removeNthFromEnd(head, n)

#head = [1]
head = ListNode(1)
n = 1
ans = Solution().removeNthFromEnd(head, n)

#head = [1,2]
head = ListNode(1)
head.next = ListNode(2)
n = 2
ans = Solution().removeNthFromEnd(head, n)