
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['8', 'x', 'x', '9', '15', '13', '11', '2', 'x', 'x'],
               ['13', 'x', 'x', 'x', '5', 'x', '7', 'x', 'x'],
               ['12', '3', 'x', 'x', 'x', 'x', 'x', '10', 'x', 'x'],
               ['12', 'x', 'x', '9', '15', '9', '11', '5', '17', 'x'],
               ['3', '5', '12', 'x', '11', '5', 'x', '15', '1', '18'],
               ['14', '3', 'x', 'x', '18', '14', '19', '19', '12', '15'],
               ['x', '20', '17', '15', '11', 'x', 'x', 'x', 'x', 'x'],
               ['12', '13', '18', 'x', 'x', '5', 'x', '2', 'x', '13'],
               ['x', 'x', '13', '19', '4', 'x', '12', 'x', 'x', '8'],
               ['x', 'x', '10', 'x', 'x', 'x', '15', 'x', '4', '16'])
   num_rows = 10
   num_cols = 10
   start = (4, 9)
   end = (6, 1)
   districts = [(0, 3), (4, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) to a neighboring workshop, provided there's no 'x' in that direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as our objective is to minimize the number of workshops visited to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end state
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # Thus the heuristic reports a lower estimate on the cost to reach the end state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring district is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved towards the end state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the end state is 0, as the distance of each district from the end state would be 0 in the end state.
   h = 0
   for district in districts:
       # Get the coordinates of the district
       district_row, district_col = district
       # Add the the Manhattan distance of the current and end coordinates of the district to the estimate
       h += abs(state[0] - district_row) + abs(state[1] - district_col)
   return h


print(a_star())
