class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        #fiding min length because we don't iterate beyond the length of the shortest string
        minlength = min(strs, key=len)

        for i in range(len(minlength)):
            m = strs[0][i]
#check if all the strings are same on the i index
            for string in strs:
                if string[i] != m:
                    return s
            s += m
        return s
