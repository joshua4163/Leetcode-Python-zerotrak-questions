class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            hashmap[char] = hashmap.get(char, 0) + 1

            while hashmap[char] > 2:
                left_char = s[left]
                hashmap[left_char] -= 1
                left += 1
        
            max_len = max(max_len, right - left + 1)
    
        return max_len