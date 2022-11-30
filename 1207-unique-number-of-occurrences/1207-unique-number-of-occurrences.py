class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        b = list(a.values())
        b.sort()
        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                return False
        return True