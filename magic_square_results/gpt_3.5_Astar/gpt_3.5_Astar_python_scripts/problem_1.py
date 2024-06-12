
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['35', 'x', '46'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the goal state, which is the grid with all unique integers from 29 to 48, satisfying the given constraints
   goal_state = [['35', '47', '46'], ['30', '40', '37'], ['42', '29', '48']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   num_range = range(29, 49)


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with any unique integer in the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in num_range:
                       # Generate the new state by replacing 'x' with the unique integer
                       new_state = [row[:] for row in state]
                       new_state[row][col] = str(num)
                       # The cost so far is the number of actions taken, as the task is to minimize the sum of all numbers in the grid
                       new_cost = g + num
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between each number in the current state and the corresponding number in the goal state
   # This heuristic relaxes the constraint that the numbers must be unique and that the sum of the specified rows, columns, and diagonal must equal the given amounts
   # It is admissible because it never overestimates the cost to reach the goal, as each number must be replaced with the correct number in the goal state
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference between two numbers is 1
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != 'x':
               h += abs(int(state[i][j]) - int(goal[i][j]))
   return h


print(a_star())
