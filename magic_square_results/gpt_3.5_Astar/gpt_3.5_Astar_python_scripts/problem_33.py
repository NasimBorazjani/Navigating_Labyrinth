
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 55]]
   # Define the goal state, which is the magic square grid with the specified sums in the rows, columns, and diagonal
   goal_state = [[31, 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 55]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3


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


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the specified range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(31, 76):
                       # Generate the new state by replacing 'x' with the unique integer
                       new_state = [row[:] for row in state]
                       new_state[row][col] = num
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all numbers
                       new_cost = g + num
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the numbers in the current state and the goal state
   # The heuristic relaxes the constraint that the numbers must be unique and within the specified range, presuming we can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a different number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum difference between the numbers in the current state and the goal state is 1
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != 'x':
               h += abs(state[i][j] - goal[i][j])
   return h


print(a_star())
