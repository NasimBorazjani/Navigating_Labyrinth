
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['6', '9', '19', 'x', '5', '9', 'x', '15', 'x'],
               ['8', '10', '16', 'x', 'x', 'x', '5', '11', '4'],
               ['5', '11', '20', '1', '14', '16', '7', '1', '5'],
               ['10', '5', '3', '5', '12', '8', 'x', 'x', '2'],
               ['16', '15', '15', '14', 'x', '13', '10', 'x', '10'],
               ['6', '4', '7', '13', 'x', 'x', 'x', 'x', '13'],
               ['x', '1', '6', '3', 'x', 'x', '17', '9', '5'],
               ['x', '11', 'x', '9', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', '18', 'x', '2', 'x', 'x', '12'])
   num_rows = 9
   num_cols = 9
   start = (1, 8)
   end = (4, 0)
   districts = [(0, 1), (2, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the workshops visited in a list; no workshops visited to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions from the current workshop
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the goal state
   # The heuristic relaxes the constraint that a district must be visited at least once
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # The heuristic is consistent because moving a district closer to the goal state reduces the heuristic cost of the successor node by a max of 1 (if the moved district is closer to the goal state), which is equal to the cost of reaching the successor node
   h = 0
   for district in districts:
       # Calculate the Manhattan distance between the current state and the district
       h += abs(state[0] - district[0]) + abs(state[1] - district[1])
       # Calculate the Manhattan distance between the district and the goal state
       h += abs(district[0] - goal[0]) + abs(district[1] - goal[1])
   return h


print(a_star())
