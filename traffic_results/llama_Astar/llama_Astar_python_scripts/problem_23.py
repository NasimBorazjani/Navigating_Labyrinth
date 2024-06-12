
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', 'x', 'x', '8', 'x', '15', '18', '10'],
               ['4', '5', '10', '6', '20', '2', '12', 'x', 'x', 'x'],
               ['19', '6', '19', '7', '6', '2', 'x', '15', 'x', '14'],
               ['16', '17', 'x', '2', '3', '7', '4', 'x', '18', '6'],
               ['x', '2', '1', '19', '7', '10', '18', '5', '3', '19'],
               ['8', '5', 'x', '1', 'x', '10', '17', 'x', '13', '5'],
               ['18', '1', '3', '4', 'x', 'x', '8', 'x', '5', 'x'],
               ['15', 'x', 'x', '13', 'x', '11', 'x', '2', 'x', 'x'],
               ['4', 'x', 'x', '4', '1', 'x', 'x', 'x', 'x', 'x'],
               ['x', '10', '8', 'x', 'x', '7', '19', 'x', 'x', 'x']]
   # Convert the city map to a 2d list of integers
   city_map = [[int(cell) if cell != 'x' else 'x' for cell in row] for row in city_map]
   start_position = (5, 8)
   end_position = (3, 0)
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   # Define the districts
   districts = [(0, 2), (3, 4), (5, 9)]


   visited_costs = {}
   visited_costs[(start_position, tuple(districts))] = 0


   queue = [(0, 0, [], (start_position, tuple(districts)))]


   while queue:
       _, g, actions, (current_position, districts_to_visit) = heapq.heappop(queue)


       # Check if the current position is the end position and all districts have been visited
       if current_position == end_position and not districts_to_visit:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in the city map
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_position = (current_position[0] + d_row, current_position[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and
               city_map[new_position[0]][new_position[1]] != 'x'):
               # Check if the new position is in a different district from the current position
               if any(start <= new_position[0] <= end for start, end in districts if start != current_position[0]):
                   # Update the districts to visit
                   new_districts_to_visit = [d for d in districts_to_visit if d[0] <= new_position[0] <= d[1]]
                   new_districts_to_visit.remove((start, end))
               else:
                   new_districts_to_visit = districts_to_visit
              
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal
               new_cost = g + city_map[new_position[0]][new_position[1]]
              
               if (new_position, tuple(new_districts_to_visit)) not in visited_costs or new_cost < visited_costs[(new_position, tuple(new_districts_to_visit))]:
                   visited_costs[(new_position, tuple(new_districts_to_visit))] = new_cost
                   # The heuristic is the sum of the distances from the current position to the end position and the remaining districts to visit
                   h = abs(new_position[0] - end_position[0]) + abs(new_position[1] - end_position[1]) + len(new_districts_to_visit)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(current_position, new_position)], (new_position, new_districts_to_visit)))
   return None


print(a_star())
