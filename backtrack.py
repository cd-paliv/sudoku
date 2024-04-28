# Steps taken to solve a sudoku using backtracking:

# Start at the first cell in the grid.
# Assign a number from 1 to 9 to the cell.
# Check if this number is valid in the current row, column, and box.
# If the number is valid, move to the next cell and repeat the process.
# If the number is not valid, increment the number and repeat the check.
# If no number can be found that is valid, it means that an error was made earlier. So, backtrack to the previous cell and increment the number there.
# Repeat this process until a solution is found or all possibilities have been exhausted.


def backtrack(board):
    # Find an empty space on the board
    find = find_empty(board)
    
    if not find:
        return True # If there are no empty spaces, the board is solved
    else:
        row, col = find

    # Try numbers from 1 to 9
    for i in range(1,10):
        # Check if the current number is valid in the current position
        if valid(board, i, (row, col)):
            # If it is, place the number
            board[row][col] = i

            # Recursively try to fill in the rest of the board
            if backtrack(board):
                return True

            # If no valid number can be found, reset the current position and backtrack
            board[row][col] = 0

    # If all numbers have been tried and none are valid, the board cannot be solved (in its current state)
    return False

# Function to check if a number is valid in a given position
def valid(board, num, pos):
    # Check the current row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the current column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the current box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# Function to find an empty space on the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None