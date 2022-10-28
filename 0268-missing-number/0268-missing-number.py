class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list([i for i,x in enumerate(nums, 1)]))-sum(nums)