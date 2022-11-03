class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        frequency = Counter(words)
        a, b = 0, 0
        for w, f in frequency.items():
            if w[0] == w[1]: 
                b = max(b, f % 2)
                a += f//2 * 2
            else:
                a += min(f, frequency[w[::-1]])
        return (a + b) * 2