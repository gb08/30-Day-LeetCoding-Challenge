"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ll_len,count = 0, 0
        ll = head
        while ll:
            ll_len += 1
            ll = ll.next
        while count != int(ll_len/2):
            head = head.next
            count +=1
        return head
