class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        m = ""
        for i in range(len(indices)):
            m += s[indices.index(i)]
        return m