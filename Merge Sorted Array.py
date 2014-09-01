#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        lena, lenb = m, n
        cura, curb = 0, 0
        while cura < lena and curb < lenb:
            if B[curb] <= A[cura]:
                incb = 0
                while curb + incb < lenb and B[curb + incb] <= A[cura]:
                    incb += 1
                for pos in range(lena - 1, cura - 1, -1):
                    A[pos + incb] = A[pos]

                for pos in range(incb):
                    A[cura + pos] = B[curb + pos]
                lena += incb
                cura += incb
                curb += incb
            else:
                cura += 1

        if curb != lenb:
            incb = lenb - curb
            for pos in range(lena - 1, cura - 1, -1):
                A[pos + incb] = A[pos]
            for pos in range(incb):
                A[cura + pos] = B[curb + pos]

if __name__ == "__main__":
    A = [1,4,4,5,6,9,0,0,0,0]
    B = [2, 3, 7, 8]
    sol = Solution()
    sol.merge(A, 6, B, 4)
    print A
