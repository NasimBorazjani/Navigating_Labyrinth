
import heapq


def initialize():
   # Define the initial state of the city as a 2d tuple
   initial_state = (('13', 'x', 'x', 'x', 'x', 'x', '8', 'x', '6'),
                   ('x', 'x', 'x', '8', '10', 'x', '17', 'x', '15', '14'),
                   ('x', '6', 'x', 'x', 'x', '16', '12', '7', '8', '11'),
                   ('x', '15', 'x', '1', '11', '19', '9', '17', 'x', 'x'),
                   ('18', '20', '16', '19', '12', '1', 'x', 'x', 'x', '5'),
                   ('11', 'x', '18', '14', 'x', '2', 'x', '9', '8', '1'),
                   ('x', '2', '5', '16', '3', '9', '2', '18', 'x', 'x'),
                   ('x', '8', '15', '17', '16', '6', 'x', '3', 'x', '10'),
                   ('3', 'x', 'x', 'x', '8', '9', '10', 'x', '6', 'x'),
                   ('6', 'x', '9', '16', '1', '3', '16', 'x', 'x', '10'))
   num_rows = 10
   num_cols = 10
   # Define the districts and their rows
   districts = [(0, 1), (2, 4), (5, 9)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie Ben has visited at least 1 workshop in each district
       if all(any(state[i][j] != 'x' for j in range(num_cols)) for i in districts):
           return actions


       # Generate all possible actions from the current state, which includes moving Ben to a neighboring workshop
       for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = 1 + dr, 1 + dc
           # Check if the new state would be valid, ie the new position must be within the bounds of the city, and the new position must not be an x
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col], new_state[1][8] = new_state[1][8], new_state[new_row][new_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to visit at least 1 workshop in each district
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, districts), new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, districts):
   # An admissible and consistent heuristic for this problem is the sum of the minimum travel times from the current position to the nearest workshop in each district
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a new district reduces the heuristic cost of the successor node by a max of 1 (if the moved district has a smaller nearest workshop), which is equal to the cost of reaching the successor node
   h = 0
   for dr, dc in districts:
       min_distance = float('inf')
       for row in range(dr, dr + 2):
           for col in range(dc, dc + 2):
               if state[row][col] != 'x':
                   min_distance = min(min_distance, int(state[row][col]))
       h += min_distance
   return h


print(a_star())
