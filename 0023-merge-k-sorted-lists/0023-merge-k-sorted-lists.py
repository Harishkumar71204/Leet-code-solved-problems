# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergel = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergel.append(self.mergelist(l1,l2))
            lists = mergel
        return lists[0]


    def mergelist(self,l1,l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return dummy.next
        