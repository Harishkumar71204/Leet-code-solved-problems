# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        cur1 = l1
        lst1 = []
        st1 = ""
        while cur1:
            lst1.insert(0,cur1.val)
            cur1 = cur1.next
        for i in lst1:
            st1 += str(i)
        f1 = int(st1)

        cur2 = l2
        lst2 = []
        st2 = ""
        while cur2:
            lst2.insert(0,cur2.val)
            cur2 = cur2.next
        for i in lst2:
            st2 += str(i)
        f2 = int(st2)
        

        sum = str(f1+f2)

        dummy = ListNode()
        cur = dummy

        for i in sum[::-1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next