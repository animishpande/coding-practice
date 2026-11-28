# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            head = None
            return head

        l = []
        while head:
            l.append(head.val)
            head = head.next

        del l[-n]
        print(l)

        head = ListNode(l[0])
        temp = head
        for i in range(1, len(l)):
            print(l[i])
            head.next = ListNode(l[i])
            head = head.next

        return temp