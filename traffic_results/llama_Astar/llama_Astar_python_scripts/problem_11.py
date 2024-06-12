
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 15, 'x', 18, 8, 6, 11, 'x', 7],
               [9, 10, 18, 9, 2, 16, 9, 8, 'x'],
               [14, 'x', 'x', 10, 18, 'x', 13, 12, 14],
               [11, 18, 4, 11, 14, 2, 20, 'x', 15],
               [12, 'x', 'x', 8, 10, 'x', 'x', 10, 11],
               [5, 19, 20, 15, 11, 'x', 14, 'x', 18],
               ['x', 5, 'x', 'x', 'x', 'x', 'x', 9, 'x'],
               ['x', 'x', 18, 'x', 'x', 4, 'x', 17, 13],
               ['x', 7, 17, 'x', 'x', 'x', 'x', 7, 19]]
   num_rows = 9
   num_cols = 9
   start = (3, 0)
   end = (4, 8)
   districts = [(0, 2), (3, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, path + [new_state], new_state))
                  
   return None


def heuristic(state, goal, districts):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances (the shortest path) of each district from the current state to the goal state
   # This heuristic relaxes the constraint that Ben must visit at least one workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district results in a decrease in the heuristic cost of the successor node by a max of the cost of moving to the district, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the cost of moving to the district) + h(n)
   h = 0
   for district in districts:
       # Calculate the Manhattan distance from the current state to the district
       h += abs(state[0] - (district[0] + district[1]) // 2) + abs(state[1] - (district[1] + district[0]) // 2)
       # Calculate the Manhattan distance from the district to the goal state
       h += abs(goal[0] - (district[0] + district[1]) // 2) + abs(goal[1] - (district[1] + district[0]) // 2)
   return h


print(a_star())
