# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_left = dummy

        for _ in range(left - 1):
            prev_left = prev_left.next

        curr = prev_left.next
        prev = None
        for _ in range(right - left + 1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        prev_left.next.next = curr
        prev_left.next = prev

        return dummy.next