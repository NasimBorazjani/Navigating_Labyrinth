
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['13', 'x', 'x', '3', '10', '20', '3', '5'],
               ['x', 'x', 'x', 'x', '20', '16', 'x', 'x', '17'],
               ['3', '14', '18', '8', '1', '20', '14', 'x', '7'],
               ['13', '3', '6', '10', '7', '4', '6', '6', '1'],
               ['10', '12', '2', 'x', '11', 'x', '10', '8', '11'],
               ['x', 'x', 'x', '11', '6', '18', '13', '20', '17'],
               ['x', 'x', '16', 'x', '4', '17', '7', '10', '15'],
               ['x', '7', '16', '6', '19', '4', '7', 'x', 'x'],
               ['x', '11', '18', 'x', 'x', 'x', '3', '8', 'x'])
   num_rows = 9
   num_cols = 9
   start_position = (5, 7)
   end_position = (2, 1)
   districts = [(0, 2), (3, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_position] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start_position], start_position)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current_position = heapq.heappop(queue)


       # Check if the current position is the end position, if so return the path taken
       if current_position == end_position:
           return path


       # Generate all possible actions from the current position, which includes moving to any of the 4 directions (north, south, east, west) if the destination is not an 'x' and the district constraint is satisfied
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_position = (current_position[0] + d_row, current_position[1] + d_col)
           # Check if the new position is valid, ie if the destination is not an 'x' and the district constraint is satisfied
           if (0 <= new_position[0] < num_rows and 0 <= new_position[1] < num_cols and
               city_map[new_position[0]][new_position[1]] != 'x' and
               any(start <= new_position[0] <= end for start, end in districts)):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal position
               new_cost = g + 1
              
               # If the new position is unvisited or we found a new path with a lower cost to reach this position, add it to the queue of not-yet-visited positions
               if new_position not in visited_costs or new_cost < visited_costs[new_position]:
                   visited_costs[new_position] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_position, end_position), new_cost, path + [new_position], new_position))
                  
   return None


def heuristic(position, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from one position to another is always the same
   # It is consistent because moving from one position to another always increases the heuristic cost of the successor node by a max of 1 (if moving to a position in the same district), which is equal to the cost of reaching the successor node
   return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


print(a_star())
