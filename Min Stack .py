#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#

class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []
        self.mincount = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minimum:
            self.minimum.append(x)
            self.mincount.append(1)
        else:
            if x < self.minimum[-1]:
                self.minimum.append(x)
                self.mincount.append(1)
            else:
                self.mincount[-1] += 1
        return x

    # @return nothing
    def pop(self):
        del(self.stack[-1])
        self.mincount[-1] -= 1
        if self.mincount[-1] == 0:
            del(self.mincount[-1])
            del(self.minimum[-1])

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.minimum[-1]
        
if __name__ == "__main__":
    ms = MinStack()
    ms.push(1)
    print ms.stack, ms.minimum, ms.mincount
    ms.push(1)
    ms.push(2)
    ms.push(-1)
    ms.push(3)
    print ms.stack, ms.minimum, ms.mincount
    ms.getMin()
    ms.top()
    ms.pop()
    print ms.stack, ms.minimum, ms.mincount
    ms.top()
    ms.pop()
    print ms.stack, ms.minimum, ms.mincount
    ms.getMin()
    
    
