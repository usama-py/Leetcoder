class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        group_length = 0
        for i in range(0, len(chars)):
            group_length += 1
            if i == len(chars) - 1:
                s.append(chars[i])
                if 10 > group_length > 1:
                    s.append(str(group_length))
                elif group_length >= 10:
                    group_length = list(str(group_length))
                    for ele in group_length:
                        s.append(ele)
            else:
                if chars[i] != chars[i + 1]:
                    s.append(chars[i])
                    if 10 > group_length > 1:
                        s.append(str(group_length))
                    elif group_length >= 10:
                        group_length = list(str(group_length))
                        for ele in group_length:
                            s.append(ele)
                    group_length = 0
        k = 0
        for ele in s:
            chars[k] = ele
            k += 1
        return len(s)
