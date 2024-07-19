class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(n))
        for src, dst in edges:
            nodes.discard(dst)
        return list(nodes)