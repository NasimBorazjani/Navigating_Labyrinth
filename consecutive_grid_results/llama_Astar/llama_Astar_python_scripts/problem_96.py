
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[81, 52, None, None], [None, 50, 53, None], [42, None, 54, 74], [None, None, 56, 77]]
   # Define the range of numbers
   num_range = range(28, 83)
   # Define the goal state, where all 'x' are replaced by unique numbers from the range
   goal_state = [[i for i in row if i is not None] for row in initial_state]
   # Define the initial cost as 0
   initial_cost = 0


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = initial_cost


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes replacing each 'x' with a unique number from the range
       for row_ind, row in enumerate(state):
           for col_ind, cell in enumerate(row):
               if cell is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique number from the range
                   new_state[row_ind][col_ind] = num_range.pop(0)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each number from its current position to its goal position
   # The heuristic relaxes the constraint that a number can only be moved to a neighboring coordinate, as it presumes we can move the numbers to their goal position by moving them to any of the other coordinates
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a number to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the number is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each number from its goal position would be 0 in the goal state.
   h = 0
   for row_ind, row in enumerate(state):
       for col_ind, cell in enumerate(row):
           if cell is not None:
               # Get goal position of the number
               goal_row_ind, goal_col_ind = [(i, j) for i in range(len(goal)) for j in range(len(goal[i])) if goal[i][j] == cell][0]
               # Add the the Manhattan distance of the current and goal coordinates of the number to the estimate
               h += abs(row_ind - goal_row_ind) + abs(col_ind - goal_col_ind)
   return h


print(a_star())
