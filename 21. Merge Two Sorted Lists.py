# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # init a dumy variable
        dummy = ListNode()
        # assign a dumy to the tail
        tail = dummy
        
        # keep going untill one of this lists still exists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
       # in case if one of the lists is not empty
        tail.next = l1 or l2

        return dummy.next
        
        
