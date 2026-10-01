# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy =ListNode(0)
        tail = dummy
        p1=list1
        p2=list2
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                tail = tail.next
                p1 = p1.next                 
            else:
                tail.next = p2
                tail = tail.next
                p2 = p2.next
        if p1:
            tail.next=p1
        else:
            tail.next=p2
        
        return dummy.next