class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            if goal == s[i:] + s[:i]:
                return True
        return False