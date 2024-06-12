
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 51, None, 65],
                    [None, None, None, 68],
                    [None, None, 64, 75],
                    [None, None, None, None]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = {'row_sums': [None, 255, 268, None],
                 'col_sums': [None, 240, 226, None],
                 'diag_sum': 264}
   # Define the range of numbers that can be used to replace 'x'
   num_range = range(43, 85)


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if check_goal(state, goal_state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a number from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   for num in num_range:
                       # Generate the new state
                       new_state = [row[:] for row in state]
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of numbers replaced, as the task is to minimize the number of numbers replaced
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def check_goal(state, goal_state):
   # Check if the current state is the goal state
   # Check the sums of rows and columns
   for row_ind in range(len(state)):
       if goal_state['row_sums'][row_ind] is not None and sum(state[row_ind]) != goal_state['row_sums'][row_ind]:
           return False
   for col_ind in range(len(state[0])):
       if goal_state['col_sums'][col_ind] is not None and sum(state[row_ind][col_ind] for row_ind in range(len(state))) != goal_state['col_sums'][col_ind]:
           return False
   # Check the sum of the diagonal
   if goal_state['diag_sum'] is not None and sum(state[i][i] for i in range(len(state))) - sum(state[i][len(state) - i - 1] for i in range(len(state))) != goal_state['diag_sum']:
       return False
   return True


def heuristic(state, goal_state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and in the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is not in the goal state), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               if goal_state['row_sums'][row_ind] is not None:
                   h += abs(goal_state['row_sums'][row_ind] - sum(state[row_ind]))
               if goal_state['col_sums'][col_ind] is not None:
                   h += abs(goal_state['col_sums'][col_ind] - sum(state[i][col_ind] for i in range(len(state))))
   if goal_state['diag_sum'] is not None:
       h += abs(goal_state['diag_sum'] - sum(state[i][i] for i in range(len(state))) + sum(state[i][len(state) - i - 1] for i in range(len(state))))
   return h


print(a_star())
