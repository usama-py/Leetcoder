class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = list(s)
        ans = ''
        if s[0] == '-':
            ans += '-'
            s = s[1:]
            
        s.reverse()
        for i in range(len(s)):
            if s[i] != '0':
                s = s[i:]
                break
        for i in range(len(s)):
            ans += s[i]
        ans = int(ans)
        if ans > 2**31-1:
            return 0
        if ans < -2**31:
            return 0
        return ans
        