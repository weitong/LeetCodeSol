#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#


class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        #str = "".join(str.split())
        if len(str) == 0:
            return 0

        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            flag = 1
            str = str[1:]
        else:
            flag = 1

        #str = str.strip()

        if len(str) == 0:
            return 0

        base, num = ord('0'), 0
        
        for i in range(len(str)):
            cur = ord(str[i]) - base
            if cur < 0 or cur > 9:
                break
            
            num = num * 10 + cur
        
        num = num * flag

        if num > 2147483647:
            return 2147483647
        elif num < -2147483648:
            return -2147483648
        else:
            return num
        
if __name__ == "__main__":
    sol = Solution()
    print sol.atoi('    3')
    print sol.atoi('-   35')
    print sol.atoi('+35dafdsafaf')
    print sol.atoi('-192375724738295826')
    print sol.atoi('  -0012a42')
    print sol.atoi('   +0 123')
    
