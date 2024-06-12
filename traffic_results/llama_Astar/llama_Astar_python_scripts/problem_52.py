
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3],
               ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17],
               [6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'],
               ['x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13],
               [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 'x', 13, 12, 20],
               [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9],
               [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'],
               ['x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'],
               [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'],
               [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'],
               ['x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 'x', 'x'],
               [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']]
   num_rows = 11
   num_cols = 12
   start = (8, 1)
   end = (5, 11)
   districts = [(0, 4), (5, 8), (9, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) from the current state, provided there's no 'x' in that direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie within the bounds of the city map and not an 'x'
           if 0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state[0]][new_state[1]] != 'x':
               # The new state is valid, generate the new state
               new_cost = g + city_map[new_state[0]][new_state[1]]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end state
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district from another district reduces the heuristic cost of the successor node by a max of 1 (if the moved district is closer to the end state), which is equal to the cost of reaching the successor node
   h = 0
   for district in districts:
       # Calculate the Manhattan distance from the current state to the end state for each district
       h += min(abs(state[0] - end[0]) + abs(state[1] - end[1]) for end in [(i, j) for i in range(district[0], district[1] + 1) for j in range(12)])
   return h


print(a_star())
