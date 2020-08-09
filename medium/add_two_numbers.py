# https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        c = 0
        d = ListNode(-1)
        dd = d
        while l1!=None and l2!=None:
            s = l1.val + l2.val + c
            if s > 9:
                s -= 10
                c = 1
            else:
                c =0
            l = ListNode(s)
            dd.next = l
            dd = l
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            s = l1.val +  c
            if s > 9:
                s -= 10
                c = 1
            else:
                c =0
            l = ListNode(s)
            dd.next = l
            dd = l
            l1 = l1.next
        
        while l2 != None:
            s = l2.val + c
            if s > 9:
                s -= 10
                c = 1
            else:
                c =0
            l = ListNode(s)
            dd.next = l
            dd = l
            l2 = l2.next

        if c > 0:
            l = ListNode(c)
            dd.next = l
            dd = l

        return d.next
            
