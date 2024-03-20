class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ""
        y = ""
        for i in word1:
            x += i
        for j in word2:
            y += j
        return x == y