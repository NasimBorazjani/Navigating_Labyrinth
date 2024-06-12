
import heapq


def a_star():
    # Define the initial state of the grid, with 'x' representing unknown values
    initial_state = [['58', '19', 'x', 'x'],
                     ['x', 'x', 'x', 'x'],
                     ['x', '22', 'x', '39'],
                     ['x', '16', '53', '29']]
    
    # Define the constraints for the sums of rows, columns, and diagonal
    row_sums = [None, 175, 114, None]
    col_sums = [None, 117, 160, None]
    diagonal_sum = 114
    
    # Encoding other variables given in the problem statement
    num_rows = 4
    num_cols = 4
    
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    
    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))
    
    while queue:
        _, g, actions, state = heappop(queue)
        
        # If the state satisfies all constraints, return the actions taken
        if check_constraints(state, row_sums, col_sums, diagonal_sum):
            return actions
        
        # Generate all possible actions from the current state, which includes replacing 'x' with unique integers
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == 'x':
                    for num in range(11, 63):
                        new_state = [row[:] for row in state]
                        new_state[i][j] = str(num)
                        new_state_str = str(new_state)
                        new_cost = g + num
                        
                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, num)], new_state))
    
    return None


def check_constraints(state, row_sums, col_sums, diagonal_sum):
    # Check if the state satisfies all constraints
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            if sum(int(state[i][j]) for j in range(len(state[i])) if state[i][j] != 'x') != row_sums[i]:
                return False
    
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            if sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x') != col_sums[j]:
                return False
    
    if sum(int(state[i][i]) for i in range(len(state)) if state[i][i] != 'x') != diagonal_sum:
        return False
    
    return True


def heuristic(state, row_sums, col_sums, diagonal_sum):
    # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the target sum
    # This heuristic relaxes the constraint that the sum of each row, column, and diagonal must be exactly equal to the target sum
    # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the target sum
    # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
    h = 0
    for i in range(len(row_sums)):
        if row_sums[i] is not None:
            h += abs(sum(int(state[i][j]) for j in range(len(state[i])) if state[i][j] != 'x') - row_sums[i])
    
    for j in range(len(col_sums)):
        if col_sums[j] is not None:
            h += abs(sum(int(state[i][j]) for i in range(len(state)) if state[i][j] != 'x') - col_sums[j])
    
    h += abs(sum(int(state[i][i]) for i in range(len(state)) if state[i][i] != 'x') - diagonal_sum)
    
    return h


print(a_star())
