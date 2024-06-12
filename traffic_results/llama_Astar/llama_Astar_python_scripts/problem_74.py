
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['10', 'x', 'x', 'x', '16', '9', 'x', '13', '12', '8', 'x', '16', '17'],
               ['9', '2', 'x', 'x', '5', 'x', 'x', 'x', '12', 'x', '3', 'x', 'x'],
               ['x', 'x', '7', '3', '12', 'x', '11', '18', '10', 'x', 'x', '13', 'x'],
               ['x', '6', 'x', '19', '2', 'x', 'x', '11', '13', '13', '1', '7'],
               ['x', 'x', '11', 'x', '16', '16', '4', '12', '5', '20', '2', '4', '15'],
               ['19', 'x', '18', '5', '11', 'x', 'x', '3', '17', '18', '3', '8', '18'],
               ['12', 'x', '9', 'x', 'x', 'x', '9', '4', '15', '16', 'x', '9'],
               ['x', '15', 'x', '6', '10', 'x', '1', '1', 'x', '9', '4', '7', '1'],
               ['x', '19', '15', 'x', '1', '10', '5', '17', 'x', '8', 'x', 'x', '1'],
               ['x', 'x', 'x', 'x', '5', 'x', '1', 'x', 'x', '7', '4', 'x', 'x'],
               ['9', 'x', '4', 'x', '5', '13', 'x', '15', 'x', 'x', '18', '9', '15'],
               ['17', '2', 'x', 'x', 'x', '18', '8', 'x', '8', 'x', 'x', '8', '7'],
               ['x', 'x', '5', 'x', 'x', '8', 'x', '8', '15', '19', 'x', 'x', 'x']]
   num_rows = 12
   num_cols = 13
   start = (3, 12)
   end = (7, 3)
   districts = [(0, 3), (4, 6), (7, 12)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the end state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the current workshop is visited at least once
       for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_row, new_col = current[0] + dr, current[1] + dc
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               all(any(0 <= new_row <= max_row and 0 <= new_col <= max_col for max_row, max_col in districts) for max_row, max_col in districts)):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + int(city_map[new_row][new_col])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
