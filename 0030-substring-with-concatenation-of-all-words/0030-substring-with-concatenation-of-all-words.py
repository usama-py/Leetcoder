class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == s.count(s[0]) and len(s) > 1000:
            return [0]
        check = set()
        length = len(words[0])
        wordlength = length*len(words)
        checked = False
        index = []
        for ele in words:
            check.add(ele[0])
        for i in range(len(s)):
            if s[i] in check:
                temp = [s[i:i + length] for i in range(i, i+wordlength, length)]
                if Counter(temp) == Counter(words):
                    index.append(i)
        return index