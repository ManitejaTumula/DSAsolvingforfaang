# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        index=1
        fcritical=-1
        lcritical=-1
        min_dist=float("inf")
        while curr and curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):
            
                if fcritical ==-1:
                    fcritical = index
                    lcritical = index
                else:
                    min_dist = min(min_dist,index-lcritical)
                    lcritical = index
            prev=curr
            curr=curr.next
            index+=1
        if fcritical == -1 or fcritical == lcritical:
            return [-1, -1]
        return [min_dist, lcritical - fcritical]
        