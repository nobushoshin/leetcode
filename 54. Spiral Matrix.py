class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_row = len(matrix)
        n_col = len(matrix[0])

        # deirections [right, down, left, up]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # add padding
        explored = [[True] * (n_col + 2) for _ in range(n_row + 2)] 
        for ri in range(n_row + 2):
            if (ri == 0) or (ri == n_row + 1):
                continue
            for ci in range(n_col + 2):
                if 1 <= ci <= n_col:
                    explored[ri][ci] = False

        # Initialize
        row, col = 0, 0
        direction = 0
        d_row, d_col = directions[direction]
        numbers = []

        for i in range(n_row * n_col):
            numbers.append(matrix[row][col])
            explored[row + 1][col + 1] = True
            # if next cell is explored, change direction.
            if explored[row + 1 + d_row][col + 1 + d_col] == True:
                direction = (direction + 1) % 4
                d_row, d_col = directions[direction]
            row += d_row
            col += d_col

        return numbers
