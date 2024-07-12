# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify code and a current node pointer
        dummy = ListNode(0)
        current = dummy
        carry = 0
        # Iterate while there are nodes in either l1 or l2, or there is a carry left
        while l1 or l2 or carry:
            # Get the current values (or 0 if we've exhausted the list)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            value = total % 10
            # Create a new node with the computed value and move the pointer
            current.next = ListNode(value)
            current = current.next
            # Move to the next nodes in l1 and l2, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # Return the next node after dummy, as the first node is a dummy node
        return dummy.next
