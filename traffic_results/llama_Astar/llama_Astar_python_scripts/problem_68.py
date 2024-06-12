
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['18', 'x', 'x', 'x', '19', 'x', 'x'],
               ['x', 'x', '8', '1', '11', 'x', 'x', 'x', 'x', '4', '6', '4'],
               ['1', '4', '15', '13', '17', '11', 'x', '15', 'x', '13', '1', 'x', 'x'],
               ['3', 'x', '6', '1', '15', '2', 'x', '13', '13', 'x', '10', 'x', 'x'],
               ['17', '12', '13', '11', '6', '1', '3', 'x', 'x', '19', '6', '6', 'x'],
               ['x', '17', '7', '12', '1', '15', '17', '20', '3', 'x', 'x', '18', '10'],
               ['16', '14', '15', 'x', 'x', '11', 'x', '17', '20', '15', '7', '10', 'x'],
               ['5', '11', 'x', '7', '19', 'x', '6', '18', '15', 'x', '8', 'x', '1'],
               ['10', 'x', '1', 'x', '6', 'x', '11', 'x', '13', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', '4', 'x', '8', 'x', '12', 'x', '12', '13', 'x'],
               ['x', 'x', '18', '14', 'x', 'x', '5', 'x', 'x', '13', '1', 'x', 'x'],
               ['x', 'x', '1', '17', '8', '18', 'x', '7', 'x', 'x', '16', '8', 'x'],
               ['x', 'x', 'x', '16', '1', 'x', '19', 'x', 'x', 'x', 'x', '14', 'x']]
   # The start and end positions of Ben
   start_pos = (5, 12)
   end_pos = (1, 2)
   # The districts in the city
   districts = [(0, 1), (2, 5), (6, 12)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_pos] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start_pos)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, current_pos = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current_pos == end_pos:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in the same district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (current_pos[0] + d_row, current_pos[1] + d_col)
           # Check if the new position is valid, ie if the new position is within the city map and there's no 'x' at the new position
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and city_map[new_pos[0]][new_pos[1]] != 'x'):
               # Check if the new position is in the same district as the current position
               if any(start <= new_pos[0] <= end for start, end in districts):
                   # The actions is valid, generate the new state
                   new_cost = g + int(city_map[new_pos[0]][new_pos[1]])
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                       visited_costs[new_pos] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_pos, end_pos), new_cost, actions + [new_pos], new_pos))
                      
   return None


def heuristic(current_pos, end_pos):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the end position
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a neighboring workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district as the new workshop), which is equal to the cost of reaching the successor node
   return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])


print(a_star())
