
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['17', 'x', 'x', 'x', '5', 'x', 'x', '12', '16', 'x', 'x', '5', '16'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '12', '4', '6', 'x', 'x'],
               ['9', 'x', 'x', 'x', 'x', 'x', '19', 'x', 'x', '13', '6', '11', '19'],
               ['1', 'x', 'x', 'x', '13', 'x', 'x', '3', '2', '7', '4', '3', 'x'],
               ['x', 'x', 'x', '14', '19', '20', '10', '13', '14', '2', 'x', '9', '3'],
               ['15', 'x', '11', '7', 'x', '11', '6', '16', 'x', 'x', 'x', '8', '19'],
               ['19', '16', '4', '8', '5', '5', '5', '11', '10', '17', '9', 'x', '5'],
               ['x', '3', '17', 'x', 'x', '6', '17', '19', 'x', 'x', '14', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', '14', 'x', '10', '14', '13', 'x', '13', 'x'],
               ['15', '5', '4', 'x', 'x', 'x', 'x', '2', '12', '6', 'x', '16', '14'],
               ['10', 'x', 'x', 'x', '9', 'x', 'x', 'x', 'x', 'x', '13', '2', 'x'],
               ['x', 'x', '17', 'x', 'x', 'x', 'x', '7', 'x', 'x', '16', 'x', 'x'],
               ['12', '10', 'x', '15', '16', 'x', 'x', '7', '11', '7', 'x', '17', 'x']]
   num_rows = 12
   num_cols = 13
   start = (1, 12)
   end = (6, 3)
   # Create the set of the valid numbers that could be in the city map
   numbers = set(range(1, 21))


   visited_costs = {}
   visited_costs[(start, tuple(city_map))] = 0


   queue = [(0, 0, [], (start, tuple(city_map)))]


   while queue:
       _, g, actions, (current_pos, city_map) = heapq.heappop(queue)


       # Check if the current position is the destination
       if current_pos == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (current_pos[0] + d_row, current_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and city_map[new_pos[0]][new_pos[1]] != 'x'):
               # Generate the new state
               new_city_map = [list(row[:]) for row in city_map]
               new_city_map[current_pos[0]][current_pos[1]] = 'x'
               new_city_map = tuple(tuple(row) for row in new_city_map)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the destination
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if (new_pos, new_city_map) not in visited_costs or new_cost < visited_costs[(new_pos, new_city_map)]:
                   visited_costs[(new_pos, new_city_map)] = new_cost
                   h = heuristic(new_pos, end)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_pos], (new_pos, new_city_map)))
   return None


def heuristic(current_pos, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the destination
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in a valid direction
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is closer to the destination), which is equal to the cost of reaching the successor node
   return abs(current_pos[0] - end[0]) + abs(current_pos[1] - end[1])


print(a_star())
