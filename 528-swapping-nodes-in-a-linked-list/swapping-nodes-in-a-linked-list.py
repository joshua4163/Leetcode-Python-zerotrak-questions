# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for i in range(k-1):
            cur = cur.next
        
        right = head
        left = cur
        while cur.next:
            cur = cur.next
            right = right.next
        right.val,left.val = left.val,right.val
        return head
