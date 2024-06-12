
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (['93', '81', '68', '57', '28', '6'],
                   ['55', '54', '58', '69', '38', '10'],
                   ['21', '_', '19', '44', '51', '18'])


   # Define the goal state
   goal_state = (['1', '2', '3', '4', '5', '6'],
                 ['7', '8', '9', '10', '11', '12'],
                 ['13', '14', '15', '16', '17', '18'])


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
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for move in moves:
                       new_i, new_j = i + move[0], j + move[1]
                       # Check if the new state is valid, ie the new position is within the bounds of the grid and not a wall
                       if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]) and state[new_i][new_j] != 'x':
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               h = heuristic(state, goal_state)
                               heapq.heappush(queue, (new_cost + h, new_cost, actions + [state[i][j]], new_state))
   return None




def heuristic(state, goal_state):
   # The heuristic function can be the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal
   return sum(abs(int(state[i][j]) - int(goal_state[i][j])) for i in range(len(state)) for j in range(len(state[i])) if state[i][j] != '_' and goal_state[i][j] != '_')




print(a_star())
