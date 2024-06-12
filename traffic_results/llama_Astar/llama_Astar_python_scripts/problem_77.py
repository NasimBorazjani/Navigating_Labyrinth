
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 5, 9, 6, 13, 13, 8, 6, 13, 'x', 13, 'x', 'x', 'x'],
               [3, 10, 16, 'x', 'x', 3, 13, 1, 11, 9, 7, 6, 'x', 18],
               [9, 11, 3, 'x', 'x', 6, 13, 'x', 14, 'x', 12, 1, 2, 4],
               ['x', 17, 13, 'x', 14, 4, 6, 8, 'x', 'x', 1, 'x', 6, 2],
               [7, 'x', 11, 'x', 14, 'x', 11, 7, 'x', 5, 'x', 1, 12, 'x'],
               ['x', 20, 20, 19, 'x', 18, 2, 19, 1, 6, 12, 'x', 'x', 16],
               [8, 5, 7, 11, 'x', 1, 'x', 'x', 'x', 11, 4, 'x', 'x', 3],
               ['x', 11, 'x', 11, 11, 'x', 18, 'x', 'x', 'x', 7, 6, 'x'],
               [2, 2, 14, 5, 5, 'x', 'x', 11, 19, 16, 'x', 14, 7, 19],
               ['x', 5, 'x', 'x', 7, 'x', 'x', 'x', 3, 15, 'x', 'x'],
               [19, 'x', 'x', 'x', 'x', 8, 3, 19, 'x', 18, 'x', 'x', 9],
               [17, 'x', 19, 'x', 'x', 'x', 5, 3, 'x', 'x', 7, 4, 'x'],
               ['x', 'x', 'x', 'x', 'x', 12, 11, 'x', 'x', 'x', 'x', 'x', 6, 6]]
   # Define the start and end positions
   start = (6, 1)
   end = (3, 13)
   # Define the districts
   districts = [(0, 1), (2, 5), (6, 13)]
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize the priority queue with the start position
   queue = [(0, 0, [], start)]


   # While there are un-visited positions
   while queue:
       # Pop the position with the lowest sum of the cost so far and estimated cost to the end position from the queue
       _, g, actions, position = heapq.heappop(queue)


       # If the current position is the end position, return the actions taken
       if position == end:
           return actions


       # Generate all possible actions from the current position, which includes moving to a neighboring position in the city map
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_position = (position[0] + d_row, position[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_position[0] < len(city_map) and 0 <= new_position[1] < len(city_map[0]) and
               city_map[new_position[0]][new_position[1]] != 'x'):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end position
               new_cost = g + city_map[new_position[0]][new_position[1]]
              
               # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of un-visited positions
               if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                   visited_costs[new_position] = new_cost
                   # The heuristic is the Manhattan distance to the end position
                   h = abs(new_position[0] - end[0]) + abs(new_position[1] - end[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_position], new_position))


                   # Check if the new position is in a different district from the start position
                   if any(start[0] >= district[0] and start[0] <= district[1] for district in districts) and any(new_position[0] >= district[0] and new_position[0] <= district[1] for district in districts):
                       # If so, remove the district from the list of districts to visit
                       districts.remove((district[0], district[1]))
   return None


print(a_star())
