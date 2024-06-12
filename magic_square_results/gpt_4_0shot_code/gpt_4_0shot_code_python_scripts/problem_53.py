
from constraint import Problem, AllDifferentConstraint

def magic_square():
    problem = Problem()

    # Add variables to the problem
    for i in range(16):
        problem.addVariable(i, range(9, 41))

    # Add constraints to the problem
    problem.addConstraint(AllDifferentConstraint())

    # Row constraints
    problem.addConstraint(lambda a, b, c, d: a + b + c + d == 94, (4, 5, 6, 7))
    problem.addConstraint(lambda a, b, c, d: a + b + c + d == 111, (8, 9, 10, 11))

    # Column constraints
    problem.addConstraint(lambda a, b: a + b == 116, (1, 5))
    problem.addConstraint(lambda a, b, c: a + b + c == 78, (2, 6, 10))

    # Diagonal constraint
    problem.addConstraint(lambda a, b, c, d: a + b + c + d == 70, (3, 6, 9, 12))

    # Known values
    problem.addConstraint(lambda a: a == 22, (2,))
    problem.addConstraint(lambda a: a == 23, (3,))
    problem.addConstraint(lambda a: a == 15, (6,))
    problem.addConstraint(lambda a: a == 25, (7,))
    problem.addConstraint(lambda a: a == 31, (8,))
    problem.addConstraint(lambda a: a == 12, (12,))
    problem.addConstraint(lambda a: a == 36, (13,))
    problem.addConstraint(lambda a: a == 13, (15,))

    # Get solutions
    solutions = problem.getSolutions()

    # Return the first solution
    return [(i // 4, i % 4, solution[i]) for i, solution in enumerate(solutions[0].items())]

print(magic_square())
