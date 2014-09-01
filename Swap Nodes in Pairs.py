#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from tools import ListNode, outputList, consList

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        
        pev, nxt = head, head.next
        pev.next = nxt.next
        nxt.next = pev
        head = nxt
        tmp = pev
        pev = pev.next
        if pev is not None:
            nxt = pev.next
        
        while pev is not None and nxt is not None:
            pev.next = nxt.next
            nxt.next = pev
            tmp.next = nxt
            tmp = pev
            pev = pev.next
            if pev is not None:
                nxt = pev.next

        return head
    
if __name__ == "__main__":
    sol = Solution()
    
    h1 = consList([])
    outputList(h1)
    h2 = sol.swapPairs(h1)
    outputList(h2)
    
    
    
