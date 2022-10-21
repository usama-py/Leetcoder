class Solution:
    def myAtoi(self, s: str) -> int:
        index = -1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0].isnumeric():
                return int(s[0])
            return 0
        for i in range(len(s)):
            if s[i].isalpha():
                return 0
            elif s[i] == '.':
                return 0
            elif s[i] == '+' or s[i] == '-':
                if s[i+1].isnumeric() == False:
                    return 0
            elif s[i].isnumeric():
                index = i
                break
        if index == -1:
            return 0
        ans = ''
        if index>0:
            if index > 1:
                if s[index-1] == '-' and s[index -2] == '-' or s[index-1] == '+' and s[index -2] == '+':
                    return 0
                if s[index-1] == '-' and s[index -2] == '+' or s[index-1] == '+' and s[index -2] == '-':
                    return 0
            if s[index-1] == '-':
                ans += '-'
        for j in range(index,len(s)):
            if s[j].isnumeric() == False:
                break
            else:
                ans += s[j]
        if int(ans) <= -2147483648:
            return -2147483648
        elif int(ans) >= 2147483648:
            return 2147483647
        return int(ans)