# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cur = head
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if n == 1:
            prev = prev.next
        else :
            temp2 = prev
            for i in range(n-2):
                temp2 = temp2.next
            temp2.next = temp2.next.next
        rcur = prev
        rprev = None
        while rcur != None:
            temp = rcur.next
            rcur.next = rprev
            rprev = rcur
            rcur = temp
        return rprev

        




