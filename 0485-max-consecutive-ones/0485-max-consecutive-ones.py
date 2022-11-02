class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        pre = 0
        for i in range(len(nums)):
            if nums[i]!=1:
                if maxi < pre:
                    maxi  = pre
                    pre = 0
                else:
                    pre = 0
            else:
                pre += 1
        if maxi > pre:
            return maxi
        return pre