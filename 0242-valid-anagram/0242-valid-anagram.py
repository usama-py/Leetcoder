class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = Counter(s)
        d = Counter(t)
        for k in c.keys():
            if c.get(k) != d.get(k):
                return False
        return True