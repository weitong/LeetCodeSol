#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        cur, prob = head, head
        while prob is not None:
            while prob is not None and prob.val == cur.val:
                prob = prob.next
            delp = cur
            while delp.next != prob:
                delp.next = delp.next.next
            cur = prob
        return head

if __name__ == "__main__":
    sol = Solution()
    def cons(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        prev = head
        for i in range(1, len(lst)):
            prev.next = ListNode(lst[i])
            prev = prev.next
        prev.next = None
        return head

    def output(head):
        cur = head
        while cur is not None:
            print cur.val,
            cur = cur.next
        print '\n'
    
    a = cons([1,1,2,3,3]) 
    output(a)
    b = sol.deleteDuplicates(a)
    output(b)
