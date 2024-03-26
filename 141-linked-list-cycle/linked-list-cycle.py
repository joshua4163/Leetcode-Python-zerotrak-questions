# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s_p = head
        f_p = head
        while f_p != None and f_p.next != None:
            s_p = s_p.next
            f_p = f_p.next.next
            if s_p == f_p:
                return True
        return False
