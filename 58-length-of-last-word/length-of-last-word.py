class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        c = 0
        for i in x[-1]:
            c += 1
        return c