# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        items = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                items.append(curr.val)
                curr = curr.next
        
        print(items)
        items.sort()
        curr = dummy = ListNode(items[0])
        for i in range(1, len(items)):
            curr.next = ListNode(items[i])
            curr = curr.next
        
        return dummy
        