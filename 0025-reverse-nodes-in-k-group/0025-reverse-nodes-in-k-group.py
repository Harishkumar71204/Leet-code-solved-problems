# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0,head)
        left = dummy
        while True:
            kth = self.getn(left,k)
            if not kth:
                break
            right = kth.next
            
            prev = kth.next
            curr = left.next
            while curr != right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tmp = left.next
            left.next = kth
            left = tmp
        return dummy.next




    def getn(self,cur,k):
        while cur and k>0 :
            cur = cur.next
            k -= 1
        return cur