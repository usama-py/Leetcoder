class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(val)
            return val
        if val > self.nums[len(self.nums)-1]:
            self.nums.append(val)
            return self.nums[-self.k]
        
        if len(self.nums) > self.k and val < self.nums[-self.k]:
            return self.nums[-self.k]
        else:
            for i in range(len(self.nums)):
                if val <= self.nums[i]:
                    self.nums.insert(i,val)
                    return self.nums[-self.k]
                


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)