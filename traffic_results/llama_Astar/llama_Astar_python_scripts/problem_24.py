
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['18', '19', '9', 'x', 'x', 'x', '3', 'x', '8', 'x'],
               ['13', '2', '3', '15', '3', 'x', '8', '9', 'x', 'x'],
               ['x', '6', '18', '1', '20', '7', '16', '8', '1', '19'],
               ['x', 'x', 'x', '20', '14', 'x', '19', '11', '9', '6'],
               ['2', 'x', 'x', '6', '5', '6', '7', '1', 'x', '8'],
               ['17', '9', '5', '3', '3', 'x', '16', '18', 'x', '8'],
               ['10', 'x', '14', '16', 'x', '8', 'x', '9', '6', 'x'],
               ['x', '17', '8', '11', '12', 'x', '4', '8', 'x', '13'],
               ['x', 'x', '6', 'x', 'x', 'x', 'x', '13', 'x', '7'],
               ['9', 'x', 'x', 'x', '3', '10', 'x', '3', '10', '1']]
   # Define the start and end positions
   start = (5, 1)
   end = (3, 9)
   # Define the districts
   districts = [(0, 3), (4, 4), (5, 9)]


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
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (state[0] + d_row, state[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and city_map[new_pos[0]][new_pos[1]] != 'x'):
               # The new position is valid, generate the new state
               new_state = new_pos
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end position
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state
   # The heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # Thus the heuristic reports a lower estimate on the cost to reach the end state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring position is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved towards the end position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the end state is 0, as the distance of each district from the end position would be 0 in the end state.
   h = 0
   for district in districts:
       # Get the position of the district
       district_pos = (max(state[0], district[0]), max(state[1], district[1]))
       # Add the the Manhattan distance of the current and end positions of the district to the estimate
       h += abs(district_pos[0] - end[0]) + abs(district_pos[1] - end[1])
   return h


print(a_star())
