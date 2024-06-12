
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['x', 7, 7, 12, 7, 'x', 13, 1, 18],
              [9, 18, 'x', 4, 19, 8, 'x', 15, 10],
              [9, 'x', 10, 5, 5, 9, 8, 'x', 'x'],
              [14, 4, 19, 9, 14, 'x', 'x', 7, 9],
              [9, 4, 11, 15, 7, 'x', 17, 3, 'x'],
              [11, 'x', 2, 18, 15, 15, 'x', 'x', 'x'],
              ['x', 5, 10, 'x', 'x', 13, 'x', 9, 'x'],
              [3, 'x', 2, 'x', 'x', 'x', 'x', 4],
              ['x', 'x', 7, 'x', 19, 'x', 'x', 'x', 9])
   num_rows = 9
   num_cols = 9
   start = (6, 1)
   end = (2, 6)
   districts = [(0, 2), (3, 5), (6, 8)]


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
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1


               # Check if the new state visits at least 1 workshop in each district
               if all(start_row <= new_row <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))


   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a district if he has visited at least one workshop in each district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a workshop in a district results in a lower heuristic cost of the successor node, which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
