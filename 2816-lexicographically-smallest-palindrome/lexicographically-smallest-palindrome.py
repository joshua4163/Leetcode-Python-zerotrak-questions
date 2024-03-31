class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        left = 0
        right = len(s) - 1
        s_list = list(s)
        while left < right:
            if s_list[left] < s_list[right]:
                s_list[right] = s_list[left]
            else:
                s_list[left] = s_list[right]
            left += 1
            right -= 1
            
        return ''.join(s_list)