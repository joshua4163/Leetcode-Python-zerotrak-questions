class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = ""
        for c in s:
            if c.isalnum():
                sen += c
        sen = sen.lower()
        return sen == sen[::-1]