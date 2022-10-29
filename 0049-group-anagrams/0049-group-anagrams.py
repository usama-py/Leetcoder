class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = defaultdict(list)
        for s in strs:   
            ana = ''.join(sorted(s))  
            anadict[ana].append(s)
        return list(anadict.values())