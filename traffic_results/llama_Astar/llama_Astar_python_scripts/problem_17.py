
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['16', '2', '16', 'x', 'x', 'x', '1', '16', 'x'],
               ['x', 'x', '19', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', '3', 'x', 'x', 'x', '10', 'x'],
               ['11', '5', '20', 'x', '1', '3', '1', 'x', '9', 'x'],
               ['x', 'x', '8', '19', 'x', 'x', 'x', '16', '15'],
               ['x', '3', '5', '10', 'x', 'x', 'x', '4', '1', 'x'],
               ['9', '18', '10', '17', '5', '6', 'x', 'x', 'x', '5'],
               ['x', 'x', '14', '5', '18', 'x', 'x', '1', '15', '1'],
               ['13', 'x', '13', '13', '14', '2', '19', '12', 'x', '1'],
               ['9', '6', 'x', '4', '12', '1', '13', '8', '2', '13'])
   num_rows = 10
   num_cols = 10
   start = (7, 9)
   end = (3, 2)
   districts = [(0, 3), (4, 6), (7, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x'):
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # Check if the new state has visited all districts
               if all(start_row <= new_row <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to the next district if he has visited at least one workshop in the current district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a new district does not change the heuristic cost of the successor node, which is equal to the cost of reaching the goal from the current state
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
