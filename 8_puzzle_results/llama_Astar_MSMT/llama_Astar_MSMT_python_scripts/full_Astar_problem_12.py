
import heapq


def initialize():
   # Define the initial state of the puzzle as a 2d tuple
   initial_state = (('66', '35', '51'),
                   ('76', '_', '73'),
                   ('90', '54', '22'))


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, visited_costs, queue
  
def a_star():
  
   initial_state, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == (('9', '8', '7'),
                   ('6', '_', '6'),
                   ('5', '4', '3'),
                   ('2', '1', '0')):
           return actions


       # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
       for i in range(3):
           for j in range(3):
               if state[i][j] == '_':
                   for new_i, new_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       # Check if the new state would be valid, ie the new_i and new_j must be within the bounds of the grid
                       if 0 <= i + new_i < 3 and 0 <= j + new_j < 3:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j], new_state[i + new_i][j + new_j] = new_state[i + new_i][j + new_j], new_state[i][j]
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                           new_cost = g + 1
                          
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # In the problem statement the tiles are indexed starting from 1, thus must add 1 to the tile number
                               heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [new_state[i + new_i][j + new_j]], new_state))
   return None




def heuristic(state):
   # The heuristic function can be the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent as the estimated cost of the next node is higher if we move the empty spot further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of tiles that can be swapped with the empty spot is by moving it to an adjacent tile, which is exactly the tile used to swap with the empty spot in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(3):
       for j in range(3):
           if state[i][j] != '_':
               goal_i, goal_j = divmod(int(state[i][j]), 3)
               h += abs(i - goal_i) + abs(j - goal_j)
   return h


print(a_star())
