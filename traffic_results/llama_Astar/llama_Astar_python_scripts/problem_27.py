
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['19', 'x', '3', 'x', 'x', '13', 'x', '12', 'x'],
               ['x', 'x', '8', 'x', '15', '18', '11', '12', 'x', '7'],
               ['x', '8', 'x', 'x', '15', '20', '17', '12', '2', '8'],
               ['x', 'x', '4', '13', '2', '14', '19', '13', '15', '19'],
               ['13', '2', 'x', '8', 'x', '17', '13', 'x', 'x', '12'],
               ['2', '20', '20', '14', 'x', 'x', '15', 'x', '2', '19'],
               ['15', '16', '18', 'x', '2', 'x', 'x', 'x', 'x'],
               ['2', 'x', '17', 'x', 'x', '12', 'x', '3', 'x'],
               ['2', 'x', '10', 'x', '6', 'x', '9', '8', '19'],
               ['17', 'x', '6', '13', 'x', '18', 'x', 'x', '18']]
   num_rows = 9
   num_cols = 10
   start = (3, 8)
   end = (6, 0)
   districts = [(0, 2), (3, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the end state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # Check if the new state has visited at least 1 workshop in each district
               if all(start_row <= new_row <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))


   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to the next district if he has visited at least 1 workshop in the current district
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a new district does not change the heuristic cost of the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
