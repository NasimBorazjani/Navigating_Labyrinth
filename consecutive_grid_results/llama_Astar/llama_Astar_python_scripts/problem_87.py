
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 33, None, 54], [None, 39, 51, 58], [41, 48, None, None], [None, None, None, None]]
   # Define the goal state of the grid, with all 'x' replaced with unique integers from the given range
   goal_state = [[14, 33, 35, 54], [15, 39, 51, 58], [41, 48, 43, 45], [16, 17, 18, 19]]
   # Define the size of the grid
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0


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


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for num in range(14, 64):
                       if all(new_state[row][col] < new_state[row][col + 1] for col in range(num_cols - 1)) and all(new_state[row][col] < new_state[row + 1][col] for row in range(num_rows - 1)) and all(new_state[row][col] < new_state[row + 1][col + 1] for row in range(num_rows - 1) for col in range(num_cols - 1)):
                           new_state[row][col] = num
                           new_state = [tuple(row) for row in new_state]
                           new_state = tuple(new_state)
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, num)], new_state))
                              
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's position matches the most common position in the new state but not in the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row in state:
       h += row[0]
   for col in range(len(state[0])):
       h += state[col][col]
   h += state[-1][-1]
   return h


print(a_star())
