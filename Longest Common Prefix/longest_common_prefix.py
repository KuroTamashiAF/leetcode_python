from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match len(strs):
            case 0:
                return ""
            case 1:
                return strs[0]

        min_length = min(map(len, strs))
        result = ""
        for i in range(0, min_length):  # 2
            current_char = strs[0][i]  # o
            for j in range(1, len(strs)):  # 3
                if current_char != strs[j][i]:  # l != l
                    return result  #
            result += current_char  # fl
        return result
