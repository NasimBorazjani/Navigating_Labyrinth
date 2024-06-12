
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing the missing numbers
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 55]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   given_sums = {'col1': 138, 'row1': 171, 'diagonal': 145}


   visited_costs = {}
   visited_costs[initial_state] = 0


   # The information we must encode for each state includes the current state of the grid and the current total cost
   # The initial state is the given grid, with a total cost of 0
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, given_sums, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, given_sums, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is a valid solution, ie if the sums of the specified rows, columns, and diagonal are equal to the given amounts
       if check_solution(state, given_sums):
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The unique integer to place is the one that makes the sum of the specified rows, columns, and diagonal equal to the given amounts
                   # This can be calculated using a simple linear equation
                   new_value = (given_sums['col1'] - (given_sums['row1'] - state[row][col] + 1) + state[row][col] - 1) // 2
                   new_state[row][col] = new_value
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of unique integers placed, as the task is to minimize the number of unique integers used
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, given_sums), new_cost, actions + [(row, col, new_value)], new_state))
   return None


def heuristic(state, given_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the unique integers must be unique and can be placed in any position
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect value must be replaced by a correct value
   # It's consistent because moving a value from one position to another reduces the heuristic cost of the successor node by a max of the difference between the given amounts and the current sums, which is equal to the cost of reaching the successor node
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] == 'x':
               # Calculate the current sum of the specified rows, columns, and diagonal
               current_sums = {'col1': sum(state[i][0] for i in range(len(state))), 'row1': sum(state[0][i] for i in range(len(state[0]))), 'diagonal': state[0][0] + state[1][1] + state[2][2]}
               # Add the absolute difference between the current sum and the given amount to the heuristic cost
               h += abs(current_sums['col1'] - given_sums['col1']) + abs(current_sums['row1'] - given_sums['row1']) + abs(current_sums['diagonal'] - given_sums['diagonal'])
   return h


def check_solution(state, given_sums):
   # Check if the sums of the specified rows, columns, and diagonal are equal to the given amounts
   current_sums = {'col1': sum(state[i][0] for i in range(len(state))), 'row1': sum(state[0][i] for i in range(len(state[0]))), 'diagonal': state[0][0] + state[1][1] + state[2][2]}
   return current_sums == given_sums


print(a_star())
