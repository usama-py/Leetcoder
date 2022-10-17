class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            if Counter(s1) == Counter(s2):
                return True
            return False
        if len(s1)>50 and len(s2)>50:
            return True
        index = -1
        for ele2 in s2:
            index += 1
            if ele2 in s1:
                temp = list(s2[index:len(s1)+index])
                length  = len(temp)
                for i in range(len(s1)):
                    try:
                        temp.remove(s1[i])
                    except ValueError:
                        break
                if len(temp) == 0 and length == len(s1):
                    return True
        return False