class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p2 = len(nums)-1
        p1 = 0
        while p1 < p2:
            if nums[p1]%2 != 0:
                if nums[p2]%2 == 0:
                    t = nums[p1]
                    nums[p1] = nums[p2]
                    nums[p2] = t
                    p2 -= 1
                    p1 += 1
                else:
                    p2 -= 1
            elif nums[p1]%2 == 0:
                p1 += 1
        return nums