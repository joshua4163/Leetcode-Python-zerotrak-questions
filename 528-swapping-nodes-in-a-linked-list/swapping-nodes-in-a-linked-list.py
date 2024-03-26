# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Find the length of the linked list
        length = get_length(head)
        
        # Handle edge cases where k is invalid
        if k < 1 or k > length:
            return head
        
        # Initialize two pointers to find the kth and (length - k + 1)th nodes
        first_pointer = head
        second_pointer = head
        for _ in range(k - 1):
            first_pointer = first_pointer.next
        for _ in range(length - k):
            second_pointer = second_pointer.next
        
        # Swap the values of the two nodes
        first_pointer.val, second_pointer.val = second_pointer.val, first_pointer.val
        
        return head        