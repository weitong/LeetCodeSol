#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n = len(A)
        for i in xrange(n):
            if target <= A[i]:
                return i
        return n

"""
Binary Search Solution by yuruofeifei
int search(int A[], int start, int end, int target) {
    if (start > end) return start;
    int mid = (start + end) / 2;
    if (A[mid] == target) return mid;
    else if (A[mid] > target) return search(A, start, mid - 1, target);
    else return search(A, mid + 1, end, target);
}
int searchInsert(int A[], int n, int target) {
    return search(A, 0, n - 1, target);
}
"""

if __name__ == "__main__":

    sol = Solution()
    print sol.searchInsert([1,3,6], 9)
    
