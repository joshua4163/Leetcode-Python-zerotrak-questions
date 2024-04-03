class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        l = 0
        r = len(s) - 1
        List = list(s)
        while l< r:
            if List[l] in vowels and List[r] in vowels:
                List[l],List[r] = List[r],List[l]
                l += 1
                r -= 1
            if List[l] not in vowels:
                l += 1
            if List[r] not in vowels:
                r -= 1
        return ''.join(List)