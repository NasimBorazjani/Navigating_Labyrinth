
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['19', 'x', '7', 'x', '12', 'x', '15', '5', '19', '14'],
               ['17', 'x', '3', '5', '7', 'x', 'x', 'x', '17', '20'],
               ['x', '11', '15', '8', 'x', '16', '4', 'x', '1', '1'],
               ['x', '8', '19', '4', '3', '3', '3', '17', '8', '15'],
               ['13', '10', '17', '17', '6', '1', 'x', '8', '13', '20'],
               ['20', 'x', 'x', 'x', 'x', '4', '18', '4', '17', 'x'],
               ['5', 'x', 'x', '10', 'x', 'x', '14', '2', '5', 'x'],
               ['7', 'x', '4', 'x', 'x', 'x', '15', 'x', 'x', 'x'],
               ['18', 'x', '18', 'x', '4', 'x', 'x', 'x', '17', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', '13', 'x', 'x'])
   num_rows = 10
   num_cols = 10
   start = (6, 0)
   end = (4, 9)
   districts = [(0, 3), (4, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the current workshop is visited
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new workshop is within the bounds of the city map, is not an 'x', and the district of the new workshop is visited
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(start_row <= new_row <= end_row for start_row, end_row in districts)):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as our objective is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, path + [new_state], new_state))
                  
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the new workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
