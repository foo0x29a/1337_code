# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)-1):
            c = m[s[i]]
            n = m[s[i+1]]
            if n > c:
                c = -c
            total += c
        total += m[s[len(s)-1]]
        return total
