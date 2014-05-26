#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        def recursion(node):
            if node.left is None and node.right is None:
                return 1
            elif node.left is None:
                return recursion(node.right) + 1
            elif node.right is None:
                return recursion(node.left) + 1
            else:
                return max(recursion(node.right), recursion(node.left)) + 1
        
        if root is None:
            return 0
        else:
            return recursion(root)
