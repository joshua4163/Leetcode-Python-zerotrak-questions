class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = []
        left = 0
        right = len(s)
        for i in s:
            if i == "I":
                l.append(left)
                left += 1
            else:
                l.append(right)
                right -= 1
        l.append(left)
        return l