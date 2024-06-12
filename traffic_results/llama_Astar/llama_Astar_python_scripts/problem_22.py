
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['2', '2', '3', 'x', '2', '10', 'x', '8', '6', 'x'],
               ['6', '11', 'x', 'x', 'x', 'x', 'x', '16', 'x', '7'],
               ['17', '17', '7', '12', '13', '15', '5', '6', '10', '13'],
               ['1', '15', '13', '3', 'x', 'x', 'x', '14', 'x', '9'],
               ['14', 'x', 'x', '6', '15', '2', '12', '18', 'x', '18'],
               ['11', '19', '1', '19', '10', '8', 'x', '14', 'x', 'x'],
               ['11', 'x', 'x', 'x', '3', 'x', 'x', '7', 'x', '2'],
               ['16', '12', 'x', 'x', 'x', '5', 'x', 'x', '10', 'x'],
               ['x', '11', 'x', '2', '12', 'x', '8', 'x', 'x', 'x'],
               ['x', 'x', '16', 'x', 'x', 'x', '16', 'x', '16', '12'])
   num_rows = 10
   num_cols = 10
   start = (1, 0)
   end = (5, 7)
   districts = [(0, 1), (2, 4), (5, 9)]


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
               if any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if (districts[i][0], districts[i][1]) not in actions):
                   # Generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # Relax the constraints on the districts to calculate the heuristic
                       h = heuristic(new_state, end, districts, city_map)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(new_state[0], new_state[1])], new_state))
   return None


def heuristic(state, end, districts, city_map):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances (the shortest path) of each district from the current state to the goal state
   # This heuristic relaxes the constraint that a district must be visited in order
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving a district closer to the goal state reduces the heuristic cost of the successor node by a max of 1 (if the moved district is closer to the goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for district in districts:
       if (district[0] <= state[0] <= district[1]) and (district[0], district[1]) not in actions:
           h += abs(state[0] - end[0]) + abs(state[1] - end[1])
   return h


print(a_star())
