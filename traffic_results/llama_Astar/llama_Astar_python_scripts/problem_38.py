
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', 3, 'x', 'x', 16, 'x', 2, 16, 3],
               [8, 'x', 8, 5, 'x', 'x', 10, 'x', 19, 4, 'x'],
               ['x', 'x', 18, 1, 16, 'x', 9, 15, 'x', 'x', 11],
               ['x', 'x', 17, 16, 4, 19, 2, 'x', 1, 11, 'x'],
               [9, 'x', 5, 16, 18, 'x', 'x', 7, 'x', 18, 6],
               ['x', 15, 7, 'x', 'x', 'x', 19, 8, 9, 17, 'x'],
               ['x', 15, 19, 'x', 'x', 'x', 6, 2, 6, 'x', 5],
               ['x', 12, 11, 3, 11, 4, 'x', 'x', 'x', 3, 'x'],
               [18, 12, 4, 'x', 3, 10, 'x', 3, 'x', 7, 14],
               [15, 11, 12, 'x', 13, 2, 'x', 'x', 5, 14, 'x'],
               ['x', 'x', 15, 'x', 16, 4, 10, 13, 'x', 'x', 4]]
   num_rows = 10
   num_cols = 11
   start = (3, 6)
   end = (8, 0)
   # Define the districts
   districts = [(0, 3), (4, 7), (8, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no x in that position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + city_map[new_row][new_col]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Check if the new state is in a different district from the start state
                   if any(start[0] >= district[0] and start[0] <= district[1] for district in districts) and any(new_row >= district[0] and new_row <= district[1] for district in districts):
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in a valid direction
   # It is admissible because it never overestimates the cost to reach the end state, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district as the current state), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
