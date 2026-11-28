# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        dup = set()

        while curr:
            if curr in dup:
                return True
            
            dup.add(curr)
            curr = curr.next

        return False
        

        