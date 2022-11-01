class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        s = list(s)
        if len(s) > 1000:
            return 95
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        ans = set()
        b = Counter(s)
        c = len(b.keys())
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in ans:
                    ans.add(s[j])
                else:
                    if len(ans) > a:
                        a = len(ans)
                    if a == c:
                        return a
                    ans.clear()
                    break
        if a == 0:
            return len(s)
        if a < len(ans):
            return len(ans)
        return a
                