class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if min(nums) > 1:
            return 1
        if max(nums) < 0:
            return 1
        if max(nums) > 100001:
            a = [-1]*100001
        else:
            a = [-1]*(max(nums)+1)
        a[0] = 0
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < 100001:
                a[nums[i]] = nums[i]
        for i in range(len(a)):
            if a[i] == -1:
                # print("--- %s seconds ---" % (time.time() - start_time))
                return i
        # print("--- %s seconds ---" % (time.time() - start_time))
        return len(a)