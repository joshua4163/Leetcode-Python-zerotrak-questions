class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            ans = max(ans, len(i.split()))
        return ans