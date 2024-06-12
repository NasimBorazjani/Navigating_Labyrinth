
import heapq


def initialize():
    # Define the initial state of the magic square, with 'x' represented as None
    initial_state = [[None, 42, None, None],
                     [None, 38, None, None],
                     [None, 36, 46, None],
                     [49, 25, 24, None]]

    # Set the constraints for the rows and columns
    row_constraints = [None, 133, 150, None]
    col_constraints = [None, 141, 134, None]
    diagonal_constraint = 155

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the moves required to get to each state in a list; no moves performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    return initial_state, row_constraints, col_constraints, diagonal_constraint, visited_costs, queue


def a_star():
    initial_state, row_constraints, col_constraints, diagonal_constraint, visited_costs, queue = initialize()

    while queue:
        _, g, moves, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is when all the constraints are satisfied and the sum of all the numbers in the grid is as low as possible
        if check_goal(state, row_constraints, col_constraints, diagonal_constraint):
            return moves

        # Generate all possible moves from the current state, which involves replacing an 'x' with a unique integer from the given range
        for row_ind in range(len(state)):
            for col_ind in range(len(state[row_ind])):
                if state[row_ind][col_ind] is None:
                    for num in range(24, 51):
                        # Check if the new state would be valid, ie the new number must not violate any of the constraints
                        if is_valid(state, row_ind, col_ind, num, row_constraints, col_constraints, diagonal_constraint):
                            # Generate the new state
                            new_state = [list(row[:]) for row in state]
                            new_state[row_ind][col_ind] = num
                            # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                            new_cost = g + 1

                            # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                            if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                                visited_costs[str(new_state)] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(state, row_constraints, col_constraints, diagonal_constraint), new_cost, moves + [(row_ind, col_ind, num)], new_state))

    return None


def heuristic(state, row_constraints, col_constraints, diagonal_constraint):
    # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
    # This heuristic relaxes the constraint that the numbers in the grid must be unique and can be in the grid only once
    # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
    # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's difference from the goal is the same in both positions), which is equal to the cost of reaching the successor node
    return sum(abs(num - goal) for row_ind, row in enumerate(state) for col_ind, num in enumerate(row) if num is not None and abs(num - row_constraints[row_ind]) + abs(num - col_constraints[col_ind]) + abs(num - diagonal_constraint if row_ind == col_ind else 0) > 0)


def check_goal(state, row_constraints, col_constraints, diagonal_constraint):
    # Check if all the constraints are satisfied
    for row_ind in range(len(state)):
        if sum(num for num in state[row_ind] if num is not None) != row_constraints[row_ind]:
            return False
    for col_ind in range(len(state[0])):
        if sum(row[col_ind] for row in state if row[col_ind] is not None) != col_constraints[col_ind]:
            return False
    if sum(state[row_ind][row_ind] for row_ind in range(len(state))) != diagonal_constraint:
        return False
    return True


def is_valid(state, row_ind, col_ind, num, row_constraints, col_constraints, diagonal_constraint):
    # Check if replacing the 'x' with the new number would violate any of the constraints
    new_state = [list(row[:]) for row in state]
    new_state[row_ind][col_ind] = num
    return check_goal(new_state, row_constraints, col_constraints, diagonal_constraint)


print(a_star())
