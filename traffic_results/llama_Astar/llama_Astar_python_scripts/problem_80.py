
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 8, 16, 3, 'x', 15, 17, 2, 'x', 'x', 5, 'x', 'x'],
               ['x', 'x', 17, 'x', 13, 'x', 13, 3, 3, 6, 11, 'x'],
               ['x', 'x', 8, 'x', 14, 1, 15, 11, 'x', 18, 12, 'x', 'x', 'x'],
               ['x', 13, 19, 4, 13, 2, 13, 3, 'x', 1, 20, 18, 'x', 15],
               [13, 'x', 1, 11, 'x', 8, 14, 4, 11, 3, 'x', 'x', 'x'],
               [12, 11, 16, 1, 1, 'x', 5, 1, 'x', 9, 'x', 'x', 1, 'x'],
               [8, 'x', 6, 15, 'x', 7, 19, 13, 2, 'x', 3, 3, 'x', 2],
               [18, 'x', 19, 15, 2, 'x', 'x', 18, 2, 'x', 10, 'x', 'x', 1],
               [3, 4, 'x', 19, 'x', 6, 'x', 7, 'x', 'x', 'x', 15, 'x'],
               ['x', 'x', 'x', 16, 7, 17, 11, 'x', 7, 'x', 'x', 'x', 'x', 15],
               ['x', 9, 'x', 'x', 'x', 19, 19, 7, 3, 12, 14, 11, 16, 7],
               [8, 19, 15, 1, 'x', 14, 'x', 1, 'x', 'x', 'x', 'x', 'x'],
               ['x', 14, 'x', 'x', 'x', 'x', 18, 'x', 'x', 2, 11, 7, 'x']]
   # Define the start and end positions
   start = (1, 10)
   end = (7, 2)
   # Define the districts
   districts = [(0, 1), (2, 6), (7, 13)]
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]


   while queue:
       _, g, actions, current = heapq.heappop(queue)


       # Check if the current position is the end position
       if current == end:
           return actions


       # Generate all possible actions from the current position
       for move in moves:
           # Calculate the new position
           new_pos = (current[0] + move[0], current[1] + move[1])
           # Check if the new position is valid
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x' and
               all(district[0] <= new_pos[0] < district[1] for district in districts)):
               # Calculate the new cost
               new_cost = g + city_map[new_pos[0]][new_pos[1]]
               # Check if the new position is unvisited or we found a new path with a lower cost
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   # Relax the constraints on the districts to calculate the heuristic
                   h = heuristic(new_pos, end, districts)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_pos))
   return None


def heuristic(current, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances to the end position and the number of districts not visited
   # This heuristic relaxes the constraint that Ben must visit at least one workshop in each district
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district that has not been visited yet reduces the heuristic cost of the successor node by a max of 1 (if the moved district has the same or fewer workshops to visit), which is equal to the cost of reaching the successor node
   h = abs(current[0] - end[0]) + abs(current[1] - end[1])
   for district in districts:
       if district[0] <= current[0] < district[1]:
           h -= 1
   return h


print(a_star())
