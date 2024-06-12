
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', '52', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the goal state, which is the grid with all unique integers from 48 to 77
   goal_state = [['48', '52', '77'], ['x', 'x', 'x'], ['x', 'x', 'x']]


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


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the range [48, 77]
       for row in range(3):
           for col in range(3):
               if state[row][col] == 'x':
                   for num in range(48, 78):
                       new_state = [row[:] for row in state]
                       new_state[row][col] = str(num)
                       # The cost so far is the number of actions taken, as the task is to minimize the sum of all numbers in the grid
                       new_cost = g + num
                       # Encode the new state as a string to store in the visited_costs dictionary
                       new_state_str = str(new_state)


                       if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                           visited_costs[new_state_str] = new_cost
                           # Add the action taken to the list of actions
                           heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between each number in the current state and the corresponding number in the goal state
   # This heuristic relaxes the constraint that each number must be unique and presumes we can move directly to the goal state by replacing 'x' with the correct numbers
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the absolute differences is always less than or equal to the sum of the numbers that need to be replaced
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference between the current and goal state is 1
   h = 0
   for i in range(3):
       for j in range(3):
           if state[i][j] != 'x':
               h += abs(int(state[i][j]) - int(goal[i][j]))
   return h


print(a_star())
