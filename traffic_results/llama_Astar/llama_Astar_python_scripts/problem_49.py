
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 13, 9, 'x', 15, 'x', 'x', 2, 13, 9, 11],
               [8, 'x', 4, 5, 13, 'x', 'x', 7, 16, 'x', 15, 13],
               ['x', 'x', 'x', 'x', 3, 'x', 4, 3, 18, 'x', 11, 18],
               [6, 'x', 14, 5, 16, 'x', 11, 'x', 3, 16, 3, 3],
               [15, 12, 'x', 'x', 10, 3, 2, 14, 'x', 18, 'x', 'x'],
               [11, 1, 2, 1, 17, 15, 'x', 2, 'x', 12, 'x', 'x'],
               ['x', 'x', 3, 15, 16, 1, 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 10, 'x', 'x', 'x', 6, 1, 8, 19, 13, 7, 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 3],
               [3, 7, 12, 'x', 15, 'x', 19, 13, 17, 14, 'x', 'x'],
               ['x', 'x', 'x', 'x', 4, 4, 18, 'x', 5, 'x', 'x', 10],
               ['x', 'x', 15, 9, 13, 10, 8, 4, 8, 6, 7, 7]]
   num_rows = 11
   num_cols = 12
   start = (3, 11)
   end = (4, 0)
   # Create the set of the valid workshops that could be visited
   workshops = {(i, j) for i in range(num_rows) for j in range(num_cols) if city_map[i][j] != 'x'}


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]


   while queue:
       _, g, actions, current = heapq.heappop(queue)


       # Check if the current position is the destination
       if current == end:
           return actions


       # Generate all possible actions from the current position
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_pos = (current[0] + dx, current[1] + dy)
           # Check if the new position is valid, ie within the city map and not a closed workshop
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and
               city_map[new_pos[0]][new_pos[1]] != 'x'):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + city_map[new_pos[0]][new_pos[1]]
               # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of un-visited positions
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   # The heuristic is the Manhattan distance to the destination
                   h = abs(new_pos[0] - end[0]) + abs(new_pos[1] - end[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], new_pos))
   return None


print(a_star())
