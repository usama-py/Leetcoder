class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        text = list(text)
        c = Counter(text)
        if c.get('b'):
            b = c.get('b')
        else:
            return 0
        if c.get('a'):
            a = c.get('a')
        else:
            return 0
        if c.get('l'):
            l = c.get('l')
        else:
            return 0
        if c.get('o'):
            o = c.get('o')
        else:
            return 0
        if c.get('n'):
            n = c.get('n')
        else:
            return 0
        
        if len(text) < 7:
            return 0
        if o == 1 or l == 1:
            return 0
        if l%2 != 0:
            l -= 1
        if o%2 != 0:
            o -= 1
        return min(b,a,n,l//2,o//2)