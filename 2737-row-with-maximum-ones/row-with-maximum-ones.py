class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        row_index = 0
        for i in range(len(mat)):
            row_count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    row_count += 1

            if row_count > max_ones:
                max_ones = row_count
                row_index = i
        return [row_index, max_ones]
