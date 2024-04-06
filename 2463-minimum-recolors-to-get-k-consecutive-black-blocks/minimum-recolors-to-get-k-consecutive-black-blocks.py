class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = float('inf')
        for i in range(len(blocks) - k + 1):
            window = blocks[i:i+k]
            count_b = window.count("B")
            recolors = k - count_b
            min_recolors = min(min_recolors, recolors)
        return min_recolors