class Solution:
    def find(self,nums, target, start, end):
        if start > end:
            return -1
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find(nums, target, start, mid - 1)
        elif nums[mid] < target:
            return self.find(nums, target, mid+1, end)
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums,target,0,len(nums)-1)