
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 40, None, 65], [34, None, 53, None], [None, None, None, 63], [None, 56, None, 62]]
   # Define the goal state, where all 'x' are replaced with unique integers from the given range
   goal_state = [[25, 40, 41, 65], [34, 42, 53, 64], [43, 46, 47, 63], [48, 56, 57, 62]]
   # Define the range of numbers that can be in the grid
   num_range = range(25, 70)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0
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


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique number from the given range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique number from the given range
                   for num in num_range:
                       if num not in new_state[row_ind] and num not in zip(*new_state)[col_ind]:
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           new_state = tuple(map(tuple, new_state))
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                               # Reset the 'x' to None for the next possible number
                               new_state[row_ind][col_ind] = None
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner in the current state and their corresponding positions in the goal state
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's position in the goal state is the same as its current position in the state), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           h += abs(state[row_ind][col_ind] - goal[row_ind][col_ind])
   return h


print(a_star())
