#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#
from tools import ListNode, consList, outputList

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        prob = prev = cur = head
        while prob is not None:
            while prob is not None and prob.val == cur.val:
                prob = prob.next

            if cur == head:
                if cur.next == prob:
                    cur = prob
                else:
                    head = cur = prev = prob
            else:
                if cur.next == prob:
                    prev = cur
                    cur = prob
                else:
                    delp = prev
                    while delp.next != prob:
                        delp.next = delp.next.next
                    cur = prob
        return head
                
if __name__ == "__main__":
    sol = Solution()
    
    a = consList([1,1,1,1,1,1]) 
    outputList(a)
    b = sol.deleteDuplicates(a)
    outputList(b)
