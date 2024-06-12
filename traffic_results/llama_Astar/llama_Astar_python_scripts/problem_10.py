
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (('x', 'x', 6, 'x', 7, 9, 4, 11),
               ('x', 3, 'x', 6, 5, 3, 15, 'x', 3),
               ('x', 'x', 'x', 4, 'x', 9, 1, 8, 'x'),
               (15, 18, 1, 6, 5, 10, 6, 14, 8),
               (18, 10, 7, 18, 2, 'x', 'x', 'x', 7),
               (11, 9, 16, 'x', 11, 'x', 11, 'x', 17),
               (7, 'x', 18, 'x', 8, 10, 20, 6, 'x'),
               (15, 4, 17, 'x', 16, 2, 12, 16, 'x'),
               (9, 10, 18, 17, 9, 6, 7, 'x', 15))
   num_rows = 9
   num_cols = 9
   start = (3, 0)
   end = (6, 6)
   districts = [(0, 3), (4, 6), (7, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path taken to reach the start state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and it's in a different district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new workshop is not an 'x' and it's in a different district
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(start_row <= new_row <= end_row for start_row, end_row in districts) and
               any(start_col <= new_col <= end_col for start_col, end_col in districts)):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a different district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a workshop in a different district reduces the heuristic cost of the successor node by a max of 1 (if the new workshop is in the same district as the old one), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
