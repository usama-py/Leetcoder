class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ele in nums:
            if count.get(ele):
                return True
            count[ele] = 1
        return False