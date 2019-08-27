# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = head
        right = head
        for i in range(n):
            right = right.next
            
        if not right:  # right已经变成了None，说明要移除的n和列表长度相同，即移除第一个节点
            return head.next
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return head
