
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', 'x', '13', 'x', 'x', '3', '8'],
               ['x', '18', '19', '19', '2', '9', 'x', 'x', 'x'],
               ['15', 'x', '6', 'x', 'x', 'x', '13', '13', '4'],
               ['7', 'x', '4', '10', 'x', '11', '10', '17', 'x'],
               ['2', '7', 'x', 'x', '8', '16', '4', '1', '4'],
               ['x', 'x', 'x', '5', '16', '15', 'x', '17', '10'],
               ['x', 'x', 'x', '5', '14', '9', '3', '15', 'x'],
               ['x', '6', '4', 'x', 'x', 'x', '18', 'x', 'x'],
               ['17', 'x', '19', 'x', '1', '4', '8', 'x', '8']]
   num_rows = 9
   num_cols = 9
   start = (2, 8)
   end = (6, 3)
   districts = [(0, 2), (3, 5), (6, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's in the same district and not a closed workshop
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is in the same district and not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts))):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as our objective is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be visited if it's in the same district, as we can move the workshops to their goal position by swapping them with any of the other workshops
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
