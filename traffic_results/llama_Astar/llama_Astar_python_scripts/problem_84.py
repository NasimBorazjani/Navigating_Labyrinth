
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 10, 16, 12, 'x', 'x', 'x', 'x', 18, 18, 10, 'x', 'x', 19],
               [7, 'x', 'x', 11, 5, 13, 6, 'x', 'x', 'x', 'x', 8, 14],
               ['x', 15, 6, 20, 4, 9, 16, 9, 16, 'x', 11, 'x', 'x', 9],
               [1, 16, 'x', 'x', 'x', 6, 15, 1, 10, 10, 9, 4, 'x', 4],
               ['x', 'x', 'x', 1, 12, 'x', 12, 17, 'x', 'x', 13, 'x', 'x', 2],
               ['x', 'x', 9, 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 10, 11],
               [7, 'x', 7, 12, 'x', 'x', 'x', 2, 2, 8, 10, 8, 'x', 'x'],
               [3, 3, 'x', 16, 11, 'x', 4, 6, 'x', 'x', 4, 17, 13, 16],
               [4, 15, 'x', 'x', 'x', 'x', 'x', 'x', 11, 19, 16, 'x', 'x', 'x'],
               [10, 5, 17, 'x', 2, 'x', 'x', 3, 10, 3, 12, 'x', 8, 'x'],
               ['x', 17, 12, 'x', 'x', 6, 2, 13, 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 10, 'x', 'x', 15, 'x', 'x', 8, 'x', 3, 'x', 'x', 19],
               [1, 7, 'x', 'x', 16, 'x', 'x', 'x', 3, 15, 10, 12, 6, 8],
               ['x', 'x', 'x', 'x', 9, 'x', 'x', 'x', 7, 'x', 'x', 'x', 'x', 8]]
   num_rows = 13
   num_cols = 14
   start = (9, 10)
   end = (2, 3)
   districts = [(0, 2), (3, 8), (9, 13)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring coordinates if it's not an 'x' and the destination district has not been visited
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new state is within the city map boundaries and the destination district has not been visited
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(start[0] <= new_row <= end[0] for start, end in districts):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to neighboring coordinates
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a neighboring coordinate is always a valid action, and the cost of reaching the successor node is equal to the cost of reaching the current node plus 1
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
