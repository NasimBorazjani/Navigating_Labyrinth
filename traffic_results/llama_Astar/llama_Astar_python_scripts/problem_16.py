
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', 16, 1, 13, 17, 7, 14, 'x'],
               ['x', 10, 'x', 12, 'x', 13, 'x', 8, 19, 4],
               [9, 13, 'x', 13, 'x', 'x', 15, 'x', 'x', 16],
               [3, 8, 'x', 16, 12, 'x', 'x', 'x', 'x', 13],
               [13, 'x', 1, 15, 18, 8, 'x', 10, 'x', 'x'],
               [8, 1, 2, 14, 'x', 8, 'x', 'x', 4, 11],
               [14, 13, 15, 'x', 16, 'x', 13, 'x', 19, 'x'],
               ['x', 4, 10, 'x', 'x', 16, 'x', 11, 'x', 'x'],
               ['x', 14, 'x', 'x', 'x', 'x', 18, 6, 18],
               ['x', 3, 2, 6, 7, 'x', 'x', 9, 8, 5]]
   # Define the start and end positions
   start = (5, 1)
   end = (3, 9)
   # Define the districts
   districts = [(0, 3), (4, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start position as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path taken to reach the start position
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end position
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring positions in the city map
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_state = (state[0] + dx, state[1] + dy)
           # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end position
               new_cost = g + city_map[new_state[0]][new_state[1]]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Relax the constraints on the districts to calculate the heuristic
                   h = heuristic(new_state, end, districts, city_map)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end, districts, city_map):
   # An admissible and consistent heuristic for this problem is the sum of the minimum travel time to reach at least one workshop in each district
   # This heuristic relaxes the constraint that Ben must visit at least one workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district results in a lower heuristic cost of the successor node, as the cost of reaching the district is the minimum travel time to reach at least one workshop in that district
   # Thus h(s) is always less than or equal to c(s, n)(equal to the minimum travel time to reach at least one workshop in the district) + h(n)
   h = 0
   for district in districts:
       # For each district, find the workshop with the minimum travel time to reach
       min_time = min(city_map[i][j] for i in range(district[0], district[1] + 1) for j in range(len(city_map[0])) if city_map[i][j] != 'x' and (i, j) not in visited_costs)
       h += min_time
   return h


print(a_star())
