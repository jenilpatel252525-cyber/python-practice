a=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # 3x3 sub-boxes (0 to 8)

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue

            # Box index from row and column
            box_index = (i // 3) * 3 + (j // 3)

            # Check if the value already exists
            if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                return False

            # Add value to row, column, and box sets
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)

    return True
