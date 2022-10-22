class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        count_a = 0
        count_b = 0
        if a == b:
            s += 'ab'*a
            return s
        for i in range(a+b):
            if a == b:
                if s[i-1] == 'b':
                    s += 'ab'*a
                else:
                    s += 'ba'*a
                return s
            if a > b:
                if count_a < 2 and a > 0:
                    s += 'a'
                    a -= 1
                    count_b = 0
                    count_a += 1
                elif b > 0:
                    s += 'b'
                    count_a = 0
                    b -= 1
                    count_b += 1
            else:
                if count_b < 2 and b > 0:
                    s += 'b'
                    b -= 1
                    count_a = 0
                    count_b += 1
                elif a > 0:
                    s += 'a'
                    count_b = 0
                    a -= 1
                    count_a += 1
        return s