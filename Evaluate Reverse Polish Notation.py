#/usr/bin/env python

# Author: Wei Tong <coding.wei@outlook.com>
#


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        ops = ["+", "-", "*", "/"]
        while True:
            for i in range(len(tokens)):
                if tokens[i] in ops:
                    if tokens[i] != "/":
                        result = eval(tokens[i-2] + tokens[i] + tokens[i-1])
                    else:
                        result = abs(int(tokens[i-2])) / abs(int(tokens[i-1]))
                        if int(tokens[i-2]) * int(tokens[i-1]) < 0:
                            result = -result
                else:
                    continue

                del(tokens[i])
                del(tokens[i-1])
                del(tokens[i-2])
                tokens.insert(i-2, str(result))
                break
            if len(tokens) == 1:
                return int(tokens[0])
s = Solution()
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
