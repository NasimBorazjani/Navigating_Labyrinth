
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing unknown values
   initial_state = [['x', 'x', 'x'], ['x', '73', '47'], ['x', 'x', 'x']]
  
   # Encoding other variables of the problem
   num_rows = 3
   num_cols = 3
   goal_sums = {'column 1': 177, 'row 1': 180, 'diagonal': 183}
   domain = list(range(34, 79))  # The domain of possible values for the unknown cells


   visited_costs = {}
   visited_costs[initial_state] = 0
          
   # The information we must encode for each state includes the current grid configuration and the sum of all numbers in the grid
   initial_state_info = (initial_state, 0)
   # The initial state has a cost of 0, as we have not replaced any 'x' with a number yet
   queue = [(0, 0, [], initial_state_info)]
  
   return initial_state, num_rows, num_cols, goal_sums, domain, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, goal_sums, domain, visited_costs, queue = initialize()
  
   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state satisfies all the given conditions, return the actions taken
       if state_satisfies_conditions(state[0], goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing each 'x' with a unique number from the domain
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[0][row_ind][col_ind] == 'x':
                   for num in domain:
                       # Generate the new state
                       new_state = list(map(list, state[0]))  # Deep copy the grid
                       new_state[row_ind][col_ind] = num
                       # Calculate the new sum of all numbers in the grid
                       new_total_sum = state[1] + num
                       # Generate the new state information
                       new_state_info = (new_state, new_total_sum)
                       # The cost of the new state is the sum of the cost so far and the cost of replacing the 'x' with the number
                       new_cost = g + cost_of_replacement(num)


                       if new_state_info not in visited_costs or new_cost < visited_costs[new_state_info]:
                           visited_costs[new_state_info] = new_cost
                           h = heuristic(new_state_info, goal_sums)
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(row_ind, col_ind, num)], new_state_info))
   return None


def state_satisfies_conditions(state, goal_sums):
   # Check if the current state satisfies all the given conditions
   # The state satisfies the conditions if the sum of the specified rows, columns, and diagonal equals the given amounts
   sums = {'column 1': sum(state[i][0] for i in range(len(state))),
           'row 1': sum(state[0]),
           'diagonal': sum(state[i][i] for i in range(len(state)))}
   return sums == goal_sums


def cost_of_replacement(num):
   # The cost of replacing an 'x' with a number is the negative of the number, as we are minimizing the sum of all numbers in the grid
   return -num


def heuristic(state_info, goal_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the given amounts
   # This heuristic relaxes the constraint that the sum of all numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node, which is equal to the cost of reaching the successor node
   sums = {'column 1': sum(state_info[0][i][0] for i in range(len(state_info[0]))),
           'row 1': sum(state_info[0][0]),
           'diagonal': sum(state_info[0][i][i] for i in range(len(state_info[0])))}
   return abs(sums['column 1'] - goal_sums['column 1']) + abs(sums['row 1'] - goal_sums['row 1']) + abs(sums['diagonal'] - goal_sums['diagonal'])


print(a_star())
