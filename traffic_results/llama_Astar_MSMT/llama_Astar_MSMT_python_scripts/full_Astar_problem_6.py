
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['6', '16', 'x', 'x', '15', 'x', '14', '11', 'x'],
               ['5', '2', '1', 'x', '3', 'x', '4', '13', 'x'],
               ['x', '7', 'x', 'x', '13', 'x', '10', '14', '5'],
               ['6', '16', 'x', '13', '6', 'x', '16', 'x', 'x'],
               ['x', '1', '17', 'x', '6', '3', 'x', 'x', '3'],
               ['11', '10', '7', '19', '15', '8', '12', '6', 'x'],
               ['18', 'x', 'x', '9', '8', '9', 'x', 'x', '13'],
               ['4', 'x', 'x', 'x', '18', '20', 'x', 'x', 'x'],
               ['x', 'x', '8', 'x', '18', '2', '6', '13', 'x']]
   start_position = (5, 5)
   end_position = (1, 0)
   num_rows = 9
   num_cols = 9
   districts = [(0, 1), (2, 4), (5, 8)]


   visited_costs = {}
   visited_costs[start_position] = 0


   queue = [(0, 0, [], start_position)]
  
   return city_map, start_position, end_position, num_rows, num_cols, districts, visited_costs, queue
  
def a_star():
  
   city_map, start_position, end_position, num_rows, num_cols, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, position = heapq.heappop(queue)


       # Check if the current position is the end position
       if position == end_position:
           return actions


       # Generate all possible actions from the current position, which includes moving to a neighboring position in the city map if it's within the bounds of the map, not an 'x', and in a different district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_position = (position[0] + d_row, position[1] + d_col)
           if (0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and
               city_map[new_position[0]][new_position[1]] != 'x' and
               any(district[0] <= new_position[0] <= district[1] for district in districts) and
               any(district[0] <= position[0] <= district[1] for district in districts)):
               # The new position must be in a different district
               if not any(district[0] <= new_position[0] <= district[1] for district in districts if district != (position[0], position[0])):
                   # Generate the new state
                   new_cost = g + int(city_map[new_position[0]][new_position[1]])
                  
                   if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                       visited_costs[new_position] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_position, end_position), new_cost, actions + [new_position], new_position))
   return None


def heuristic(position, end_position):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the end position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from one position to another is always equal to or less than the actual cost
   # It's consistent because moving from one position to another always increases the heuristic cost of the successor node by a max of 1 (if moving to a position in the same district), which is equal to the cost of reaching the successor node
   return abs(position[0] - end_position[0]) + abs(position[1] - end_position[1])


print(a_star())
