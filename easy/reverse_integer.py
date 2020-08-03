# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            r = int(str(x)[-1::-1])
        else:
            r = -int(str(-x)[-1::-1])
        
        if abs(r) > (1<<31)-1:
            return 0
        return r
