class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        max_len = []
        for index, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if index >= len(word) or word[index] != letter:
                    return "".join(max_len)
            max_len.append(letter)
                
        return "".join(max_len)
