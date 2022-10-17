class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if s[i] == ' ':
                for j in range(i-1,-1,-1):
                    if s[j] != " ":
                        ans += s[j]
                    else:
                        break
                ans += ' '
            if i == len(s)-1 and s[i] != ' ':
                for i in range(len(s)-1,-1,-1):
                    if s[i] == ' ':
                        break
                    else:
                        ans += s[i]
        
        print(ans)
        return ans