#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def helper(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            return helper(a.left, b.right) and helper(a.right, b.left)
        if root is None:
            return True
        else:
            return helper(root.left, root.right)

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(3)
    n7 = TreeNode(4)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n7, n6
    sol = Solution()

    n = TreeNode(1)
    print sol.isSymmetric(n1)
        
