from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum elements in each row
        min_in_rows = {min(row) for row in matrix}

        # Step 2: Transpose the matrix to find maximum elements in each column
        transposed_matrix = list(zip(*matrix))
        max_in_cols = {max(col) for col in transposed_matrix}

        # Step 3: The intersection of min_in_rows and max_in_cols will give us the lucky numbers
        lucky_nums = list(min_in_rows & max_in_cols)

        return lucky_nums
