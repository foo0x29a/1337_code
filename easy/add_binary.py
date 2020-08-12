# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        r = []
        
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        
        while len(a) > len(b):
            b = (len(a)-len(b))*[0] + b

        while len(a) < len(b):
            a = (len(b)-len(a))*[0] + a

        p1 = len(a)-1
        

        while p1 >=0:
            s = a[p1] ^ b[p1] ^ c
            c = (a[p1] & b[p1]) | (b[p1] & c) | (a[p1] & c)
            r.append(str(s))
            p1 -= 1
        
        if c == 1:
            r.append("1")

        return "".join(r[::-1])
