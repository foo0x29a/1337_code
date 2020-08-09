# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        m = 0
        f = {}
        for end in range(len(s)):
            c = s[end]
            
            if c in f:
                start = max(start, f[c] + 1)
            f[c] = end
            m = max(m, end - start + 1)

        return m
