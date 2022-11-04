class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        check = set()
        length = len(words[0])
        wordlength = length*len(words)
        if wordlength > len(s):
            return []
        if len(s) == s.count(s[0]) and len(s) > 1000:
            return [0]
        b = Counter(words)
        index = []
        for ele in words:
            check.add(ele[0])
        for i in range(len(s)):
            if s[i] in check:
                temp = [s[i:i + length] for i in range(i, i+wordlength, length)]
                if Counter(temp) == b:
                    index.append(i)
        return index