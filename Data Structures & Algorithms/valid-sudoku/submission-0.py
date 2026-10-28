class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # 1. Check all rows
        for row in board:
            d = {}

            for num in row:
                if num == '.':
                    continue

                if num in d:
                    return False

                d[num] = 1

        # 2. Check all columns
        for col in range(9):
            d = {}

            for row in range(9):
                num = board[row][col]

                if num == '.':
                    continue

                if num in d:
                    return False

                d[num] = 1

        # 3. Check all 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                d = {}

                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]

                        if num == '.':
                            continue

                        if num in d:
                            return False

                        d[num] = 1

        return True