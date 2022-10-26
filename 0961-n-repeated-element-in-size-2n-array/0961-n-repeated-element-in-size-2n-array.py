class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        a = [0]*10000
        for i in range(n+1):
            a[nums[i]] += 1
            if a[nums[i]] > 1:
                return nums[i]
        return nums[n+1]