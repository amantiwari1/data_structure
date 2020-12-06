# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if  l1.val == 0 and l1.next == None and l2.next == None and l2.val == 0:
            return ListNode(0)
        a = l1.val
        b = l2.val
        c = (a+b)//10
        
        
        nodes = ListNode((a+b)%10)
        stores = nodes
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2= l2.next
          
            nodes.next = ListNode((a+b+c)%10)
            c = (a+b+c)//10
            nodes = nodes.next
                
        if nodes.val == 0 or a+b >= 10:
            nodes.next = ListNode(1)
        return stores 
            
            