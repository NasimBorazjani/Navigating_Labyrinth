
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid represented as a 2D tuple
   initial_state = (('x', 46, 'x'), (39, 'x', 'x'), ('x', 'x', 'x'))
   # Define the goal state, which is the sum of the specified rows, columns, and diagonal
   goal_state = (124, 126, 136)
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(28, 58))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies the goal state, return the actions taken
       if check_goal_state(state, goal_state):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for num in unique_integers:
                       new_state = [list(row) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       new_cost = g + num
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(i, j, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current sum of rows, columns, and diagonal and the goal sum
   # The heuristic relaxes the constraint that the numbers must be unique and that the sum of the numbers in the grid must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be made up by the unique integers in the grid
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is the difference between the current sum and the goal sum, which is exactly the decrease in the heuristic estimate
   h = 0
   for i in range(3):
       # Calculate the sum of each row and compare it to the goal sum
       row_sum = sum(state[i])
       h += abs(row_sum - goal[i])
       # Calculate the sum of each column and compare it to the goal sum
       col_sum = sum(row[i] for row in state)
       h += abs(col_sum - goal[i])
   # Calculate the sum of the diagonal from top right to bottom left and compare it to the goal sum
   diagonal_sum = sum(state[i][2-i] for i in range(3))
   h += abs(diagonal_sum - goal[2])
   return h


def check_goal_state(state, goal):
   # Check if the current state satisfies the goal state, ie the sum of the specified rows, columns, and diagonal equals the given amounts
   for i in range(3):
       if sum(state[i]) != goal[i]:
           return False
       if sum(row[i] for row in state) != goal[i]:
           return False
   if sum(state[i][2-i] for i in range(3)) != goal[2]:
       return False
   return True


print(a_star())
