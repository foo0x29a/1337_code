# https://leetcode.com/problems/maximum-subarray/submissions/
# Kadane's Algorithm
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        g = -math.inf
        l = -math.inf
        
        for i in nums:
            l = max(i, l+i)
            g = max(l, g)
        return g
        
