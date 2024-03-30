class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
    
    # Iterate over each word and reverse it
        for i in range(len(words)):
            words[i] = words[i][::-1]
    
    # Join the reversed words back together with space
        return ' '.join(words)