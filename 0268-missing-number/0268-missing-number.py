class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list([i for i,x in enumerate(nums, 1)]))-sum(nums)
        # a = [-1]*(max(nums)+1)
        # for i in range(len(nums)):    
        #     a[nums[i]] = nums[i]
        # for i in range(len(a)):
        #     if a[i] == -1:
        #         return i
        # return len(a)