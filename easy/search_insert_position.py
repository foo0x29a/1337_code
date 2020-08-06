import math
class Solution:
    def search(self, nums, target, start, end):
        if start > end:
            return start
        mid = math.floor((end + start)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return self.search(nums, target, start, end)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search(nums, target, 0, len(nums)-1)
