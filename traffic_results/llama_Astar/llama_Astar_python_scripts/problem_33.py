
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['16', '10', 'x', '16', '1', '12', '6', '12', '3', '7', 'x'],
               ['x', '16', '10', '9', '12', '19', '7', '10', '12', '13', '7'],
               ['5', 'x', '9', 'x', '5', '16', '16', '8', 'x', '16', '8'],
               ['x', '4', '14', 'x', 'x', 'x', 'x', 'x', '7', '18'],
               ['13', '12', '16', '14', 'x', '2', '4', '2', 'x', '6', '3'],
               ['x', '11', '20', 'x', 'x', 'x', '1', 'x', 'x', '9', 'x'],
               ['x', 'x', '8', '10', 'x', 'x', '3', '1', 'x', 'x', '6'],
               ['x', '2', '9', 'x', '8', '13', 'x', 'x', 'x', '12', '11'],
               ['12', 'x', '2', 'x', 'x', '1', 'x', '15', 'x', '1'],
               ['3', 'x', 'x', 'x', '17', 'x', '18', '4', '1', 'x'],
               ['x', 'x', '6', 'x', 'x', '12', 'x', 'x', 'x', '15', '12'])
   num_rows = 10
   num_cols = 11
   start = (2, 10)
   end = (5, 2)
   districts = [(0, 1), (2, 4), (5, 10)]


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


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
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
   # The heuristic relaxes the constraint that a district must be visited in a specific order
   # Thus the heuristic reports a lower estimate on the cost to reach the end state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring district is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved towards the end state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the end state is 0, as the distance of each district from the end state would be 0 in the end state.
   h = 0
   for district in districts:
       # Get the Manhattan distance between the current state and the district
       h += abs(state[0] - district[0]) + abs(state[1] - district[1])
       # Get the Manhattan distance between the district and the end state
       h += abs(district[0] - end[0]) + abs(district[1] - end[1])
   return h


print(a_star())
