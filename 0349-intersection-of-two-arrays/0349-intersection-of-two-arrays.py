class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(Counter([ele for ele in nums1 if ele in nums2]).keys())
        