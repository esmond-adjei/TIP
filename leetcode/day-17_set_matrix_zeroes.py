from typing import List

# Problem: Set Matrix Zeroes
# concept: in-place modification

# approach 1: naively store the rows and columns that have zeros
# then iterate through the matrix and set the rows and columns to zero
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []

        nr, nc = len(matrix), len(matrix[0])
        for r in range(nr):
            for c in range(nc):
                if matrix[r][c] == 0:
                    zero_cols.append(c)
                    zero_rows.append(r)

        for r in range(nr):
            for c in range(nc):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

# approach 2: use the first row and column to store the zero rows and columns
# then iterate through the matrix and set the rows and columns to zero
# 1. record the zero state of the first row and column
# 2. create markers in the first row and column to store the zero state of the other rows and columns
# 3. iterate through the (sub)matrix and set the markers in the first row and column
# 4. use record state of the first row and column to set the other rows and columns to zero
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nr, nc = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][c] == 0 for c in range(nc))
        first_col_has_zero = any(matrix[r][0] == 0 for r in range(nr))

        # Use first row and column to mark zero rows and columns
        for r in range(1, nr):
            for c in range(1, nc):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # Set matrix cells to zero based on markers
        for r in range(1, nr):
            for c in range(1, nc):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the first row if needed
        if first_row_has_zero:
            for c in range(nc):
                matrix[0][c] = 0

        # Zero out the first column if needed
        if first_col_has_zero:
            for r in range(nr):
                matrix[r][0] = 0