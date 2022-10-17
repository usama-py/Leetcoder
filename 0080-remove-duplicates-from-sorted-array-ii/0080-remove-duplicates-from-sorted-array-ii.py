class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        temp = nums[0]
        extra = 0
        for i in range(len(nums)):
            if temp != nums[i]:
                extra = 1
                temp = nums[i]
                nums[k] = temp
                k+=1
            elif extra < 2 and nums[i] == temp:
                nums[k] = temp
                extra += 1
                k+=1
        return k