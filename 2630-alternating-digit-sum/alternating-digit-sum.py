class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        for i in range(len(s)):
            if i % 2 == 0:
                ans += int(s[i])
            else:
                ans -= int(s[i])
        return ans