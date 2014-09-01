#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        tmp = None
        head, tail = 0, len(A) - 1
        while head < tail:
            if A[head] == 0:
                if A[tail] == 0:
                    pass
                elif A[tail] == 1:
                    pass
                elif A[tail] == 2:
                    tail -= 1
                head += 1
            elif A[head] == 1:
                if A[tail] == 0:
                    A[head], A[tail] = 0, 1
                    head += 1
                elif A[tail] == 1:
                    if tmp is None:
                        tmp = tail
                    while tail != head and A[tail] == 1:
                        tail -= 1
                    if tail == head:
                        pass
                    else:
                        if A[tail] == 2:
                            A[tail], A[tmp] = 1, 2
                            tmp = max(tail, tmp - 1)
                        elif A[tail] == 0:
                            A[head], A[tail] = 0, 1
                            head += 1
                elif A[tail] == 2:
                    tail -= 1
            elif A[head] == 2:
                if A[tail] == 0:
                    A[head], A[tail] = 0, 2
                    head += 1
                    tail -= 1
                elif A[tail] == 1:
                    if tmp is not None and tmp > tail:
                        A[head], A[tmp] = 1, 2
                        tmp -= 1
                    else:
                        A[head], A[tail] = 1, 2
                        tail -= 1
                        if tmp is not None:
                            tmp -= 1
                elif A[tail] == 2:
                    tail -= 1

"""
Smarter One:

xianlei 
 public void sortColors(int[] A) {


    int i=-1, j=-1, k=-1;

    for(int p = 0; p < A.length; p++)
    {
        if(A[p] == 0)
        {
            A[++k]=2;
            A[++j]=1;
            A[++i]=0;
        }
        else if (A[p] == 1)
        {
            A[++k]=2;
            A[++j]=1;

        }
        else if (A[p] == 2)
        {
            A[++k]=2;
        }
    }

}

 riccardo
{ public void sortColors(int[] A) {

    int i=-1, j=-1;

    for(int p = 0; p < A.length; p++) {

       int v = A[p];
       A[p] = 2;

       if (v == 0) {

          A[++j] = 1;
          A[++i] = 0;
       }
       else if (v == 1) {

           A[++j] = 1;
       }
    }
}
}

jizhilong 
void sortColors(int A[], int n) {
  int i = 0, j = n-1;
  for (int k = 0; k <= j; k++) {
    switch (A[k]) {
      case 0:
        A[k] = 1;
        A[i++] = 0;
        break;
      case 1:
        break;
      case 2:
        A[k--] = A[j];
        A[j--] = 2;
        break;
    }
  }
}
"""
                
if __name__ == "__main__":   
    sol = Solution()
    A = [1,2,2,2,2,0,0,0,1,1]
    sol.sortColors(A)
    print A
    
