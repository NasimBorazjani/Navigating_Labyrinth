
import heapq


def a_star():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('87', '49', '79', '68', '_'),
                   ('56', '19', '64', '37', '7'),
                   ('27', '15', '41', '35', '78'))
   num_rows = 3
   num_cols = 5


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == tuple(tuple(str(i) for i in range(8, 0, -1)) + ('_',)):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 4 neighboring tiles
       for row in range(num_rows):
           for col in range(num_cols):
               # Check if the new state would be valid, ie the empty spot must not move off the grid
               if row > 0 and state[row][col] == '_':
                   temp_state = [list(row[:]) for row in state]
                   temp_state[row][col], temp_state[row - 1][col] = temp_state[row - 1][col], temp_state[row][col]
                   new_state = tuple(tuple(row) for row in temp_state)
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
               elif row < num_rows - 1 and state[row][col] == '_':
                   temp_state = [list(row[:]) for row in state]
                   temp_state[row][col], temp_state[row + 1][col] = temp_state[row + 1][col], temp_state[row][col]
                   new_state = tuple(tuple(row) for row in temp_state)
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
               elif col > 0 and state[row][col] == '_':
                   temp_state = [list(row[:]) for row in state]
                   temp_state[row][col], temp_state[row][col - 1] = temp_state[row][col - 1], temp_state[row][col]
                   new_state = tuple(tuple(row) for row in temp_state)
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
               elif col < num_cols - 1 and state[row][col] == '_':
                   temp_state = [list(row[:]) for row in state]
                   temp_state[row][col], temp_state[row][col + 1] = temp_state[row][col + 1], temp_state[row][col]
                   new_state = tuple(tuple(row) for row in temp_state)
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] != '_':
               goal_row, goal_col = divmod(int(state[row][col]) - 1, num_cols)
               h += abs(row - goal_row) + abs(col - goal_col)
   return h


print(a_star())
