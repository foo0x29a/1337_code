# https://leetcode.com/problems/count-and-say/submissions/
class Solution:
    def aux(self, start, end, c):
        if start == end:
            return c
        count = 0
        ref = c[0]
        l = []
        for i in c:
            if i == ref:
                count += 1
            else:
                l.append(str(count))
                l.append(ref)
                ref = i
                count = 1
        l.append(str(count))
        l.append(i)
        return self.aux(start+1, end, "".join(l))
        
    def countAndSay(self, n: int) -> str:
        return self.aux(1, n, "1")