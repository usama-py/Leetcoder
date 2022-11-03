class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    ans -= 1
                else:
                    ans += 1
            elif s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    ans -= 10
                else:
                    ans += 10
            elif s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    ans -= 100
                else:
                    ans += 100
        if s[len(s)-1] == 'I':
            ans += 1
        elif s[len(s)-1] == 'X':
            ans += 10
        elif s[len(s)-1] == 'C':
            ans += 100
        a = Counter(s)
        for k,v in a.items():
            if k == 'V':
                ans += 5*v
            elif k == 'L':
                ans += 50*v
            elif k == 'D':
                ans += 500*v
            elif k == 'M':
                ans += 1000*v
        return ans