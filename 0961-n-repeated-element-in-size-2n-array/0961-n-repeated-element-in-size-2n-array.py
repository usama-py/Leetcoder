class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a = Counter(nums)
        ans = 0
        for k,v in a.items():
            if v > 1:
                return k