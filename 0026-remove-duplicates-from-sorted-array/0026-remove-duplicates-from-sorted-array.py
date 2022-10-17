class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        temp = nums[0]
        for i in range(len(nums)):
            if nums[i] != temp:
                k += 1
                nums[k] = nums[i]
                temp = nums[i]
        return k+1