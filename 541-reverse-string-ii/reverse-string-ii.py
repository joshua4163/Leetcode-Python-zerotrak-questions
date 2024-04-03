class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l, r = 0, k 
        s = list(s)
        if len(s) <= k:
            s = s[::-1]
            return ''.join(s)
        while l < len(s):
            s[l:r] = reversed(s[l:r])           
            l += 2*k
            r += 2*k 
        return ''.join(s)        