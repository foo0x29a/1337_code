# https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")[-1]
        return len(s)
