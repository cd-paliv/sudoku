import numpy as np
from backtrack import backtrack

class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints

def AC3(csp):
    queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
    while len(queue) != 0:
        (Xi, Xj) = queue.pop(0)
        if revise(csp, Xi, Xj): # If values were removed from the domain of Xi
            if not csp.domains[Xi]: # If the domain of Xi is empty, the CSP cannot be solved
                return False
            # If the domain of Xi was revised, enqueue all arcs (Xk, Xi) where Xk is a neighbor of Xi
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

# Remove values from Xi's domain that don't have a consistent extension to Xj
def revise(csp, Xi, Xj):
    revised = False
    for x in csp.domains[Xi]:
        # If there's no value in the domain of Xj that satisfies the constraint between Xi and Xj
        if not any(csp.constraints(Xi, x, Xj, y) for y in csp.domains[Xj]):
            # Remove the value from the domain of Xi
            csp.domains[Xi].remove(x)
            revised = True
    return revised

class AC3_Sudoku:
    def __init__(self, board):
        self.board = board
        self.csp = self.create_csp()

    def create_csp(self):
        variables = np.arange(81)
        domains = {}
        for v in variables:
            if self.board[v//9][v%9] != 0:  # if the cell has value pre-defined
                domains[v] = [self.board[v//9][v%9]]  # set its domain to its value
            else:
                domains[v] = list(range(1, 10))  # otherwise, set its domain to all possible values
        # The neighbors of a cell are the cells in the same row, column, or 3x3 square
        neighbors = {v: [n for n in self.get_neighbors(v)] for v in variables}
        # The constraint between two cells is that they must have different values
        constraints = self.different_values_constraint
        return CSP(variables, domains, neighbors, constraints)

    def get_neighbors(self, v):
        # Calculate the row and column of the cell
        row = v // 9
        col = v % 9
        # Calculate the row and column of the 3x3 square that the cell belongs to
        square_row = row // 3
        square_col = col // 3

        row_indices = [9*row + i for i in range(9)]
        col_indices = [9*i + col for i in range(9)]
        square_indices = [9*(square_row*3 + i//3) + square_col*3 + i%3 for i in range(9)]

        neighbors = set(row_indices + col_indices + square_indices)
        neighbors.remove(v) # Remove the index of the cell itself

        return list(neighbors)

    def different_values_constraint(self, Xi, x, Xj, y):
        return x != y
    
    def solve(self):
        used_backtracking = False
        if AC3(self.csp):
            unsolved = []
            for v in self.csp.variables:
                if len(self.csp.domains[v]) == 1:
                    self.board[v//9][v%9] = self.csp.domains[v][0]
                else:
                    unsolved.append(v)

            if unsolved:  # If there are cells left with multiple possible values
                for v in unsolved:
                    for value in self.csp.domains[v]:
                        self.board[v//9][v%9] = value
                        if not backtrack(self.board):
                            self.board[v//9][v%9] = 0
                        else:
                            used_backtracking = True
                            break
                    if not used_backtracking:
                        return None, used_backtracking

            return self.board, used_backtracking
        else:
            return None, used_backtracking

    # def solve(self): # Apply the AC3 algorithm to the CSP
    #     used_backtracking = False
    #     if AC3(self.csp):
    #         for v in self.csp.variables:
    #             if len(self.csp.domains[v]) == 1:
    #                 self.board[v//9][v%9] = self.csp.domains[v][0]
    #             else:
    #                 if not backtrack(self.board):
    #                     return None, used_backtracking
    #                 used_backtracking = True
    #         return self.board, used_backtracking
    #     else:
    #         return None, used_backtracking