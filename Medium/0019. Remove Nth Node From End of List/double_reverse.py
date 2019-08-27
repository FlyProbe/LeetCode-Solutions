'''
Not good enough!
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def reverse(head):
            now = head
            pre = None
            while now:
                temp = now.next
                now.next = pre
                pre = now
                now = temp
            head = pre
            return head
        
        head = reverse(head)
        now = head
        if n == 1:
            return(reverse(head.next))
        else:
            for i in range(n-2):
                now = now.next
            now.next = now.next.next
            head = reverse(head)
            return head
