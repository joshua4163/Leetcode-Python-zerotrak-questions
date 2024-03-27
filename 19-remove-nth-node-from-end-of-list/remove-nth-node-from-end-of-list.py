# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(node):
            c = 0
            while node:
                c += 1
                node = node.next
            return c

        total_length = length(head)

        if n == total_length:
            return head.next #null will be there
            
        cur = head
        for _ in range(total_length - n -1):
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        return head