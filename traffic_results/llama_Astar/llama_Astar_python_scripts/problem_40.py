
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 10, 'x', 8, 13, 8, 4, 3, 15, 'x', 17],
               [9, 'x', 6, 4, 17, 'x', 16, 3, 19, 'x', 'x'],
               [8, 3, 18, 'x', 'x', 3, 'x', 7, 12, 16, 17],
               [8, 'x', 'x', 13, 'x', 7, 'x', 8, 'x', 12, 9],
               [2, 9, 'x', 'x', 9, 4, 18, 'x', 'x', 11, 'x'],
               [14, 20, 'x', 'x', 'x', 'x', 10, 'x', 'x', 7, 'x'],
               ['x', 'x', 18, 16, 12, 10, 'x', 'x', 10, 'x', 'x'],
               ['x', 'x', 16, 'x', 'x', 10, 'x', 'x', 3, 18, 18],
               ['x', 'x', 'x', 'x', 'x', 13, 3, 'x', 'x', 'x', 'x'],
               [5, 13, 1, 'x', 'x', 8, 'x', 19, 'x', 'x', 'x'],
               ['x', 'x', 16, 'x', 'x', 7, 18, 4, 11, 'x', 16]]
   num_rows = 10
   num_cols = 11
   start = (3, 10)
   end = (5, 1)
   districts = [(0, 1), (2, 4), (5, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) from the current state, provided there's no 'x' in that direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new state is within the bounds of the city map and there's no 'x' in that direction
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the goal state
   # The heuristic relaxes the constraint that a district must be visited at least once
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved toward the goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each district from its goal position would be 0 in the goal state.
   h = 0
   for district in districts:
       h += abs(state[0] - district[0]) + abs(state[1] - district[1])
   return h


print(a_star())
