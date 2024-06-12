
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' as a placeholder for hidden numbers
   initial_state = [['x', 51, 'x'], [48, 50, 'x'], ['x', 'x', 'x']]


   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   grid_range = range(22, 76)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, grid_range, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, num_rows, num_cols, grid_range, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique number from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique number from the grid_range
                   number_to_replace = new_state[row_ind][col_ind] = grid_range.pop(0)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state 
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, number_to_replace)], new_state))
                      
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each number from its current position to its goal position in the grid
   # The heuristic relaxes the constraint that a number can only be moved to another position in the grid if the position is marked with an 'x', and presumes we can move the numbers to their goal position by moving them to any other position in the grid
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a number from one position to another is always 1, which is exactly the decrease in the Manhattan distance, if the number is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each number from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "x" when finding the goal position of each number
           if state[i][j] != 'x':
               # Get goal position of each number
               goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the number to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
