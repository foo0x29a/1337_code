class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sz = len(needle)
        if sz == 0:
            return 0
        
        start = 0
        
        for end in range(len(haystack)):
            if end >= sz -1:
                if haystack[start:end+1] == needle:
                    return start
                start +=1
        return -1
