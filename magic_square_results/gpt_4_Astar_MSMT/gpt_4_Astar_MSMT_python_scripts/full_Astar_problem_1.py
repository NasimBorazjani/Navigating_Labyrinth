
import heapq

def initialize():
    # Define the initial state of the grid, the goal sums of the specified row, column, and diagonal, and the range of unique integers that can be used to replace 'x's
    initial_state = (('35', 'x', '46'), ('x', 'x', 'x'), ('x', 'x', 'x'))
    goal_sums = {'row1': 103, 'col1': 107, 'diag': 124}
    num_range = set(range(29, 49))

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    return initial_state, goal_sums, num_range, visited_costs, queue

def a_star():
    # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, the goal sums, and the range of unique integers)
    initial_state, goal_sums, num_range, visited_costs, queue = initialize()

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        # The goal state is where the sum of the specified row, column, and diagonal equal the goal sums, and there are no 'x's in the grid
        if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == goal_sums['row1'] and sum(int(state[i][1]) for i in range(3)) == goal_sums['col1'] and sum(int(state[i][2-i]) for i in range(3)) == goal_sums['diag']:
            return actions

        # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
        if any(cell == 'x' for row in state for cell in row):
            # Find the next 'x' in the grid
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 'x':
                        # Generate the set of available numbers by subtracting the set of numbers present in the current state from the set of all numbers in the range
                        available_nums = num_range - set(int(cell) for row in state for cell in row if cell != 'x')
                        for num in available_nums:
                            # Generate the new state
                            new_state = [list(row) for row in state]
                            new_state[i][j] = str(num)
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                            new_cost = g + num

                            # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
                        # Stop searching for 'x's after the first 'x' is found and all possible actions from it are generated
                        break
                else:
                    continue
                break
    return None

def heuristic(state, goal_sums):
    # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums and the goal sums of the specified row, column, and diagonal
    # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of all of the numbers in the grid must be minimized; ie It presumes we can add or subtract any amount to the current sums to reach the goal sums
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of reaching a successor node is the number added to the grid, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums
    h = 0
    if any(cell == 'x' for row in state for cell in row):
        h += abs(sum(int(cell) for cell in state[1] if cell != 'x') - goal_sums['row1'])
        h += abs(sum(int(state[i][1]) for i in range(3) if state[i][1] != 'x') - goal_sums['col1'])
        h += abs(sum(int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x') - goal_sums['diag'])
    return h

print(a_star())
