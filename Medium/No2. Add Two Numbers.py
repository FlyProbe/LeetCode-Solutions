# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        elif not l1:
            return l2
        else:
            
            
            r1 = l1
            r2 = l2
            count = 0
            while l2 and l1:
                l2.val += l1.val
                l2.val += count
                if l2.val > 9:
                    l2.val -= 10
                    count = 1
                else:
                    count = 0
                x = l2
                l2 = l2.next
                l1 = l1.next
            if l1:
                l2 = l1
                x.next = l2
                while l2 and count!=0:
                    l2.val += count
                    if l2.val > 9:
                        l2.val -= 10
                        count = 1
                    else:
                        count = 0
                    x = l2
                    l2 = l2.next
            elif l2:
                while l2 and count!=0:
                    l2.val += count
                    if l2.val > 9:
                        l2.val -= 10
                        count = 1
                    else:
                        count = 0
                    x = l2
                    l2 = l2.next
            if count != 0:
                l2 = ListNode(self)
                l2.val = 1
                l2.next = None
                x.next = l2
            return r2
