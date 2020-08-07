# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Slow and Fast Pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
