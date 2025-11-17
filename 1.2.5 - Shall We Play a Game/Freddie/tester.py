def get_next_open_row(board, col, ROW_COUNT):
     for r in range(ROW_COUNT):
          if board[r][col] == 0:  # Assuming 0 represents an empty cell
               return r
          return -1  # Indicates the column is full

def drop_piece(board, row, col, piece):
        board[row][col] = piece

ROW_COUNT = 6
COLUMN_COUNT = 7
board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)] # Initialize empty board

# Player 1 drops a chip in column 3
selected_column = 3
next_row = get_next_open_row(board, selected_column, ROW_COUNT)
if next_row != -1:
    drop_piece(board, next_row, selected_column, 1) # Place Player 1's chip
    print(f"Chip placed at row {next_row}, column {selected_column}")
else:
    print(f"Column {selected_column} is full.")
    