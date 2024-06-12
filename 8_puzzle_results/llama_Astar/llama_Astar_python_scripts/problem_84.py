
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (['85', '96', '29', '80', '12'],
                   ['60', '_', '76', '42', '82'],
                   ['27', '89', '72', '37', '55'])
   # Define the goal state
   goal_state = (['1', '2', '3', '4', '5'],
                 ['6', '7', '8', '9', '10'],
                 ['11', '12', '13', '14', '15'])
   # Define the possible moves
   moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for row in range(len(state)):
           for col in range(len(state[row])):
               if state[row][col] == '_':
                   for move in moves:
                       new_row, new_col = row + move[0], col + move[1]
                       # Check if the new state is valid, ie the new position is within the bounds of the grid
                       if 0 <= new_row < len(state) and 0 <= new_col < len(state[row]):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[row][col]], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of the cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               goal_row, goal_col = divmod(int(state[i][j]) - 1, len(state[i]))
               h += abs(i - goal_row) + abs(j - goal_col)
   return h




print(a_star())
