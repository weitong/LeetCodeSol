#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

from tools import ListNode, consList, outputList

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is not None:
            fast, slow = head, head
            while fast is not None and fast.next is not None:
                fast, slow = fast.next.next, slow.next
            hh = slow.next
            slow.next = None
            
            if hh is not None and hh.next is not None:
                prv, cur, nxt = None, hh, hh.next
                while cur is not None:
                    nxt = cur.next
                    cur.next = prv
                    prv = cur
                    cur = nxt
                hh = prv
                
            h = head
            while hh is not None:
                cur = hh
                hh = hh.next
                cur.next = h.next
                h.next = cur
                h = cur.next
            
            
class NaiveSolution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is not None:
            h, t = head, head
            while t.next is not None:
                t = t.next

            while h != t and h.next != t:
                cur, t = t, h
                while t.next != cur:
                    t = t.next
                t.next = None

                cur.next = h.next
                h.next = cur
                h = cur.next
    
if __name__ == "__main__":
    h = consList([1,2,3,4])
    sol = Solution()
    sol.reorderList(h)
    outputList(h)
