
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['19', '7', '11', 'x', '3', '18', '8', 'x', 'x', 'x', 'x'],
               ['12', '18', '6', '1', '13', '12', '14', '11', '13', '5', '19'],
               ['11', '10', '10', '18', '15', 'x', '12', 'x', '4', '17', '10'],
               ['4', '3', '3', '7', 'x', '19', 'x', 'x', 'x', '12', '9'],
               ['x', 'x', '6', '19', 'x', '4', '14', 'x', '9', '4', '15'],
               ['4', '7', '6', '5', '8', 'x', '15', '3', 'x', '16', '3'],
               ['13', 'x', 'x', '1', '9', '1', '9', 'x', 'x', 'x', 'x'],
               ['2', '13', '5', '9', '5', 'x', '6', 'x', '18', 'x', '3'],
               ['19', 'x', '2', '9', '4', '13', 'x', 'x', 'x', '16', '6'],
               ['x', 'x', 'x', '12', 'x', '7', '9', '3', '9', '8', '1'],
               ['x', '10', 'x', '12', '3', '6', 'x', '4', '12', '4', 'x']]
   # Define the start and end positions
   start = (5, 10)
   end = (3, 0)
   # Define the districts
   districts = [(0, 3), (4, 4), (5, 10)]


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


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, districts, city_map):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end position
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved district is closer to the end position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for district in districts:
       # Calculate the Manhattan distance from the current state to the end position and the district
       h += abs(state[0] - end[0]) + abs(state[1] - end[1]) + abs(state[0] - district[0]) + abs(state[1] - district[1])
   return h


print(a_star())
