#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
		self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            pass
        else:
            parent = root
            next = parent.left
            while parent is not None and next is not None:
                prev = None
                while parent is not None:
                    if prev is None:
                        prev = parent.left
		    else:
                        prev.next = parent.left
                        prev = prev.next
                    prev.next = parent.right
                    prev = prev.next
                    parent = parent.next
                parent = next
                next = parent.left
				
class ShortSolution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            pass
        else:
            pre, cur = root, None
            while pre.left is not None:
                cur = pre
                while cur is not None:
                    cur.left.next = cur.right
                    if cur.next is not None:
                        cur.right.next = cur.next.left
                    cur = cur.next
                pre = pre.next
			
				
	
