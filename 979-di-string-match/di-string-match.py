class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        low, high = 0, n
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        # At the end, low and high will be the same
        result.append(low)
        return result