class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = Counter(nums)
        for v in a.values():
            if v > 1:
                return True
        return False