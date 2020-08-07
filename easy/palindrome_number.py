# https://leetcode.com/problems/palindrome-number/
# Two Pointers
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        start = 0
        end = len(s) - 1

        while s[start] == s[end]:
            if start >= end:
                return True
            start += 1
            end -= 1
            
        return False
