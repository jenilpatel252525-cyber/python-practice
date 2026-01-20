def solveSudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            if board[3*(r//3) + i//3][3*(c//3) + i%3] == ch:
                return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for ch in '123456789':
                        if is_valid(r, c, ch):
                            board[r][c] = ch
                            if solve():
                                return True
                            board[r][c] = '.'  # backtrack
                    return False  # no valid digit found
        return True

    solve()