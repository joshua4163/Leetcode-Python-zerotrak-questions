# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            swap1 = prev.next
            swap2 = prev.next.next

            prev.next = swap2
            swap1.next = swap2.next
            swap2.next = swap1

            prev = swap1

        return dummy.next
