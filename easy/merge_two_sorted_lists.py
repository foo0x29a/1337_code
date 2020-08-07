# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge Sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll = ListNode(-1)
        l = ll
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l.next = l1
                l = l1
                l1 = l1.next
            else:
                l.next = l2
                l = l2
                l2 = l2.next

        while l1 != None:
            l.next = l1
            l = l1
            l1 = l1.next
            
        while l2 != None:
            l.next = l2
            l = l2
            l2 = l2.next
        
        return ll.next
            
