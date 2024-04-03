class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '' or len(s) == 1:
            return True
        
        s = s.lower()
        clean_text = "".join(char for char in s if char.isalnum())
        left = 0
        right = len(clean_text) - 1
        while left < right:
            if clean_text[left] != clean_text[right]:
                return False
            left += 1
            right -= 1
        return True
