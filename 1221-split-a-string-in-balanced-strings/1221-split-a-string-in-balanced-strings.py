class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = list(s)
        ans = 0
        count_r = 0
        count_l = 0
        for i in range(len(s)):
            if s[i] == 'R':
                count_r += 1
            else:
                count_l += 1
            if count_r == count_l:
                ans += 1
        return ans