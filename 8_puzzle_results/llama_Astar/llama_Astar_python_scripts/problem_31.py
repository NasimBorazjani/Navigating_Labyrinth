
import heapq


def a_star():
   # Define the initial state of the puzzle
   initial_state = (['75', '53', '73', '62'],
                   ['_', '14', '90', '43'],
                   ['21', '17', '51', '27'])
   # Define the goal state
   goal_state = (['8', '7', '6', '5'],
                 ['4', '3', '2', '1'],
                 ['_', '_', '_', '_'])
   # Convert the states to tuples for immutability
   initial_state = tuple(tuple(row) for row in initial_state)
   goal_state = tuple(tuple(row) for row in goal_state)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves swapping the empty spot with any of the 4 neighboring tiles
       for i in range(len(state)):
           for j in range(len(state[i])):
               if state[i][j] == '_':
                   for d_i, d_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       new_i, new_j = i + d_i, j + d_j
                       # Check if the new state would be valid, ie the new state must be within the bounds of the grid
                       if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]):
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
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != '_':
               goal_i, goal_j = next(((gi, gj) for gi, row in enumerate(goal_state) for gj, cell in enumerate(row) if cell == state[i][j]), None)
               h += abs(i - goal_i) + abs(j - goal_j)
   return h




print(a_star())
