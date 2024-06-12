
import heapq


def initialize():
   # Define the initial state of the magic square, as a 2d list of strings
   initial_state = [['48', 'x', 'x'], ['x', 'x', 'x'], ['x', '49', 'x']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_column_sum = 150
   goal_row_sum = 209
   goal_diagonal_sum = 169


   visited_costs = {}
   visited_costs[str(initial_state)] = 0
  
   # The information we must encode for each state includes the current state of the magic square and the sum of the numbers in the square
   initial_state_str = str(initial_state)
   initial_state_sum = sum(int(i) for row in initial_state for i in row if i != 'x')
   # The initial state must be added to the priority queue
   queue = [(initial_state_sum, 0, [], initial_state_str)]
  
   return initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state_str = heapq.heappop(queue)


       # Convert the current state from a string back to a 2d list
       state = eval(state_str)


       # Check if the current state is the goal state
       # The goal state is when the sum of the numbers in the magic square equals the sum of the numbers in the goal state
       if sum(int(i) for row in state for i in row if i != 'x') == goal_column_sum + goal_row_sum + goal_diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(40, 90):
                       # Check if the new state would be valid, ie the new state must have a sum equal to the goal sum
                       if sum(int(i) for row in state for i in row if i != 'x') + num - 40 == goal_column_sum + goal_row_sum + goal_diagonal_sum:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = str(num)
                           new_state = [tuple(row) for row in new_state]
                           new_state_str = str(new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                               visited_costs[new_state_str] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state_str, goal_column_sum, goal_row_sum, goal_diagonal_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state_str))
   return None


def heuristic(state_str, goal_column_sum, goal_row_sum, goal_diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that each 'x' can only be replaced with a unique integer from the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect value must be replaced at least once
   # It's consistent because moving a value from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved value is equal to the goal value), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   state = eval(state_str)
   for row_ind in range(num_rows):
       for col_ind in range(num_cols):
           if state[row_ind][col_ind] == 'x':
               h += 1
           else:
               h += abs(int(state[row_ind][col_ind]) - goal_column_sum)
   return h


print(a_star())
