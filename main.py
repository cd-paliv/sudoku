from backtrack import backtrack
from ac3 import *
from dokusan import generators
import numpy as np
import time

def main():
    print("\nSudoku Solver")
    print("-------------------------\n")
    
    sudoku = generators.random_sudoku(avg_rank=150)
    sudoku_string = str(sudoku)
    board = np.array([int(char) for char in sudoku_string]).reshape(9,9)
    print("Sudoku board:")
    print_board(board)
    #print(renderers.colorful(sudoku))

    print("\n-------------------------")
    print("\nChoose the solving method:")
    print("1. Backtracking")
    print("2. AC3")
    print("3. Both")
    choice = input("Enter your choice: ")

    # Solve the board
    print("\nSolving the Sudoku board...\n")
    start_time = time.time()

    if choice == '1':
        if backtrack(board):
            print("Sudoku board solved successfully!\n")
            print_board(board)
        else:
            print("No solution exists for the given Sudoku board.\n")
    
    elif choice == '2':
        solution, used_backtracking = AC3_Sudoku(board).solve()
        if solution is not None:
            print("Sudoku board solved successfully using AC3", end="")
            print(" (backtracking was used to finish solving the board)\n" if used_backtracking else "!\n")
            print_board(board)
        else:
            print("No solution exists for the given Sudoku board using AC3.\n")

    elif choice == '3':
        start_time_3 = time.time()
        if backtrack(board):
            print("Sudoku board solved successfully using backtracking!\n")
            print_board(board)
        else:
            print("No solution exists for the given Sudoku board using backtracking.\n")
        end_time_3 = time.time()
        elapsed_time = end_time_3 - start_time_3
        print("\nBacktracking elapsed time:", elapsed_time, "seconds")
        print("\n-------------------------")
        
        start_time_3 = time.time()
        solution, used_backtracking = AC3_Sudoku(board).solve()
        if solution is not None:
            print("\nSudoku board solved successfully using AC3", end="")
            print(" (backtracking was used to finish solving the board)\n" if used_backtracking else "!\n")
            print_board(board)
        else:
            print("No solution exists for the given Sudoku board using AC3.\n")
        end_time_3 = time.time()
        elapsed_time = end_time_3 - start_time_3
        print("\nAC3 elapsed time:", elapsed_time, "seconds")
        print("\n-------------------------")

    else:
        print("Invalid choice.\n")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nElapsed total time:", elapsed_time, "seconds\n")

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Call the main function
if __name__ == "__main__":
    main()