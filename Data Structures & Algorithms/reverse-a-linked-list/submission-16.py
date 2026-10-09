# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            # [None, 0, 1, 2, 3] -> [None, 3, 2, 1, 0]
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev