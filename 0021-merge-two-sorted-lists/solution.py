# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            if not l1:
                return l2
            if not l2:
                return l1
        else:
            output = ListNode(0)
            current = output
            while l1 and l2:
                if l1.val > l2.val:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    l1 = l1.next
                current = current.next
            if l1:
                current.next = l1
            elif l2:
                current.next = l2
            return output.next
            
