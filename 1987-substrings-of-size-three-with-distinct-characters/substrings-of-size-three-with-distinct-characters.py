class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for r in range(len(s) - 3 + 1):
            window = s[r:r+3]
            if len(set(window)) == 3:
                count += 1
        return count
