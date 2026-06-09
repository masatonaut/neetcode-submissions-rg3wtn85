# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        vals[left-1:right] = vals[left-1:right][::-1]
        node = head
        for v in vals:
            node.val = v
            node = node.next
        return head