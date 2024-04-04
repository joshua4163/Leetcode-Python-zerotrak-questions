class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = right = 0
        seen = set()
        c = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            if len(seen) == 3:
                c += 1
                seen.remove(s[left])
                left += 1
            right += 1
        return c