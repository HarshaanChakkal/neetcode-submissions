# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, val=0, next=None):
  #      self.val = val
   #     self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [none -> 0 -> 1 -> 2 -> 3 -> none]
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            # 0 --> None and 1 does not have anything pointing to it
            prev = curr
            curr = temp
        curr = prev
        return curr
