
from constraint import Problem, ExactSumConstraint, AllDifferentConstraint

# Create a problem instance
problem = Problem()

# Define the variables and their possible values
variables = [(i, j) for i in range(4) for j in range(4)]
problem.addVariables(variables, range(35, 62))

# Add the constraints for the given numbers in the grid
problem.addConstraint(lambda a: a == 37, [(1, 1)])
problem.addConstraint(lambda a: a == 41, [(1, 3)])
problem.addConstraint(lambda a: a == 48, [(2, 0)])
problem.addConstraint(lambda a: a == 49, [(3, 0)])
problem.addConstraint(lambda a: a == 46, [(3, 2)])
problem.addConstraint(lambda a: a == 38, [(3, 3)])

# Add the constraints for the sums of the rows and columns
problem.addConstraint(ExactSumConstraint(180), [(1, j) for j in range(4)])
problem.addConstraint(ExactSumConstraint(176), [(2, j) for j in range(4)])
problem.addConstraint(ExactSumConstraint(151), [(i, 1) for i in range(4)])
problem.addConstraint(ExactSumConstraint(189), [(i, 2) for i in range(4)])

# Add the constraint for the sum of the diagonal
problem.addConstraint(ExactSumConstraint(184), [(i, 3-i) for i in range(4)])

# Add the constraint that all numbers must be different
problem.addConstraint(AllDifferentConstraint())

# Get the solutions
solutions = problem.getSolutions()

# Print the solutions
for solution in solutions:
    print([(k[0], k[1], v) for k, v in solution.items()])
