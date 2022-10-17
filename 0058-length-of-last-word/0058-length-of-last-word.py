class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s)
        a = 0
        b = False
        for i in range(len(s)-1,-1,-1):
            if i == len(s)-1 and i == ' ':
                b = True
            elif s[i] != ' ' and b == True:
                a += 1
            elif s[i] != ' '  and b == False:
                a += 1
            if s[i] == ' ' and a>0:
                break
            print(i)
        return a
            