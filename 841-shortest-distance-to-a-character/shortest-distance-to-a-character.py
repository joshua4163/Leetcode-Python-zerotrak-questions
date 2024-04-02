class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        k = []
        m = 0
        for i in range(len(s)):
            if s[i] == c:
                l.append(i)

        for j in range(len(s)):
            if m < len(l) - 1 and abs(j - l[m]) > abs(j - l[m+1]):
                m += 1
            k.append(abs(j - l[m]))
        return k
