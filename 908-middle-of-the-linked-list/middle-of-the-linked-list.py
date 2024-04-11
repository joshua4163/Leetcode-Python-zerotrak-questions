# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_p = head
        f_p = head
        while f_p and f_p.next:
            s_p = s_p.next
            f_p = f_p.next.next
        return s_p
