
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', '4', '6', 'x', '9', '15', '11', '2'],
               ['19', 'x', '14', '3', '10', '18', 'x', 'x', 'x', '1'],
               ['x', '9', 'x', '11', '7', '14', 'x', 'x', '16', '18'],
               ['x', '5', '4', '5', '2', '4', '7', '5', '19', '14'],
               ['x', '3', '20', 'x', '5', '16', 'x', 'x', '1', '9'],
               ['x', '3', '15', '9', '4', 'x', 'x', 'x', 'x', '4'],
               ['11', '18', '19', '8', '17', '9', 'x', '10', '10', '19'],
               ['x', 'x', 'x', '17', '7', 'x', 'x', '7', '12', '8'],
               ['x', 'x', '11', '19', 'x', '13', '10', '13', 'x', 'x'],
               ['18', 'x', 'x', 'x', '6', '10', '7', 'x', '8', 'x']]
   num_rows = 10
   num_cols = 10
   start = (3, 9)
   end = (6, 1)
   districts = [(0, 3), (4, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the current workshop is visited
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city map and is not an 'x'
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Check if the district of the new workshop has been visited
               if any(district[0] <= new_row <= district[1] for district in districts):
                   # Generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                      
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be visited if it's in the same district as the current workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
