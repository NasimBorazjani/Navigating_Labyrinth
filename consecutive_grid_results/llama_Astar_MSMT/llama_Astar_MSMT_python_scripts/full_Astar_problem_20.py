
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' replaced by '_' for easier processing
   initial_state = [['80', '_', '_'], ['56', '_', '64'], ['51', '_', '76']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 48
   range_end = 91


   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # The information we must encode for each state includes the current state of the grid and the current cost
   # The initial state of the grid is the given initial state, and the initial cost is 0
   initial_state = (initial_state, 0)
   # The priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the grid is filled with unique integers and the numbers in the topmost row, rightmost column, and diagonal sum to the minimum
       if is_goal_state(state):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[0][row][col] == '_':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state[0]]
                   for num in range(range_start, range_end + 1):
                       if num not in new_state[row] and num not in new_state[col] and num not in new_state[row][col:]:
                           new_state[row][col] = num
                           new_state = (new_state, g + 1)
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, rightmost column, and diagonal
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and must only appear once in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the difference between the two numbers, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the difference between the two numbers) + h(n)
   h = 0
   for row in state[0]:
       h += sum(map(int, row))
   return h


def is_goal_state(state):
   # Check if the grid is filled with unique integers and the numbers in the topmost row, rightmost column, and diagonal sum to the minimum
   # The grid is filled with unique integers if there are no 'x's left
   if '_' in state[0]:
       return False
   # The numbers in the topmost row, rightmost column, and diagonal must sum to the minimum
   if sum(map(int, state[0][0])) + sum(map(int, state[0][i][-1] for i in range(len(state[0])))) + sum(map(int, state[0][i][i] for i in range(len(state[0])))) != 3 * (range_start + range_end) // 2:
       return False
   return True


print(a_star())
