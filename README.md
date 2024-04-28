## Description
This code is a Sudoku solver that uses either one or both the AC3 and Backtracking algorithms.

### AC3 (Arc-Consistency 3 Algorithm)
AC3 is a constraint propagation algorithm used in constraint satisfaction problems. It works by iteratively removing values from the domain of variables that are not consistent with the constraints. However, AC3 only guarantees arc-consistency, meaning that for every single constraint, there is some way to satisfy it. It does *not* guarantee that a global solution exists that satisfies all constraints simultaneously.

### Backtracking
Backtracking is a search algorithm that finds a solution by trying out all possible paths of the problem until it finds a solution or exhausts all possibilities. In the context of Sudoku, it tries different numbers in each cell until it finds a combination that satisfies all Sudoku rules.

### Sudoku
The solver first applies the AC3 algorithm to simplify the Sudoku puzzle as much as possible. AC3 works by ensuring that all the domains (possible values for each cell) are consistent with the Sudoku rules. However, it may not be able to solve the puzzle completely because while all domains are consistent, they might not be reduced to a single value. In other words, there may still be cells left with multiple possible values even after applying AC3.

In such cases, the solver uses Backtracking to try different values for the remaining cells until it finds a solution or determines that no solution exists. Backtracking is capable of finding a solution even when AC3 fails to do so because it checks the global consistency of the board, not just the local consistency of each cell.

The solver also provides the option to solve the Sudoku puzzle using only the Backtracking algorithm, without applying AC3 first.

## How to use
1. Clone repo
2. Execute `python3 main.py`
3. Select the desired way to solve the sudoku
4. Get solution