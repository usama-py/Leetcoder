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
            elif s[i] == 'M':
                ans += 1000
            elif s[i] == 'V':
                ans += 5
            elif s[i] == 'L':
                ans += 50
            else:
                ans += 500
        i = len(s)-1
        if s[i] == 'I':
            ans += 1
        elif s[i] == 'X':
            ans += 10
        elif s[i] == 'C':
            ans += 100
        elif s[i] == 'M':
                ans += 1000
        elif s[i] == 'V':
            ans += 5
        elif s[i] == 'L':
            ans += 50
        else:
            ans += 500
        
        return ans