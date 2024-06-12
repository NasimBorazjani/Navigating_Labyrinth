
from ortools.sat.python import cp_model

def magic_square():
    model = cp_model.CpModel()

    # Create variables
    grid = [[model.NewIntVar(28, 59, f'x{i}{j}') for j in range(4)] for i in range(4)]
    grid[0][0] = 50
    grid[0][3] = 42
    grid[2][0] = 47
    grid[2][2] = 49
    grid[3][0] = 53
    grid[3][3] = 30
    grid[1][2] = 44

    # Add constraints
    model.Add(sum(grid[1]) == 185)
    model.Add(sum(grid[2]) == 162)
    model.Add(sum(grid[i][1] for i in range(4)) == 134)
    model.Add(sum(grid[i][2] for i in range(4)) == 166)
    model.Add(sum(grid[i][3-i] for i in range(4)) == 173)

    # All cells must be different
    model.AddAllDifferent([grid[i][j] for i in range(4) for j in range(4) if isinstance(grid[i][j], cp_model.IntVar)])

    # Solve model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution
    if status == cp_model.OPTIMAL:
        for i in range(4):
            for j in range(4):
                if isinstance(grid[i][j], cp_model.IntVar):
                    print(f'({i}, {j}, {solver.Value(grid[i][j])})')

magic_square()
