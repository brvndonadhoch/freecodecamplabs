def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []

    def dfs(row, current_solution, cols, diag1, diag2):
        if row == n:
            solutions.append(list(current_solution))
            return
        
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue
            
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            current_solution.append(col)

            dfs(row +1, current_solution, cols, diag1, diag2)

            current_solution.pop()
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
    dfs(0, [], set(), set(), set())

    return solutions
    
"""usage
dfs_n_queens(5)"""