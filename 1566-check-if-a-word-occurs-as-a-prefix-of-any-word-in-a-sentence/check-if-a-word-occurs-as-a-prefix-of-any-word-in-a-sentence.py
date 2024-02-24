class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for idx in range(len(words)):
            if words[idx].startswith(searchWord):
                return idx + 1
        return -1