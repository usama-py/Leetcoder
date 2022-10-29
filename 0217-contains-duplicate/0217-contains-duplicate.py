class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ele in nums:
            if ele in count:
                return True
            count[ele] = 1
        return False