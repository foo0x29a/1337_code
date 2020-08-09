# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = int("".join(str(d) for d in digits))
        i+=1
        return list(str(i))
