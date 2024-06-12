
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['15', '19', '13', '4', 'x', 'x', '13', '7', '16', '6', 'x', 'x', '17', 'x'],
               ['2', '2', 'x', '7', 'x', '12', '12', 'x', '19', 'x', '10', '4', '14', '2'],
               ['11', 'x', 'x', '3', '7', 'x', '7', 'x', '6', 'x', '19', 'x', '1'],
               ['x', 'x', '11', 'x', '3', 'x', '17', 'x', '10', '2', '18', '7', '15', '1'],
               ['x', 'x', '13', 'x', '12', '17', '5', '4', 'x', '16', '9', 'x', '19', '14'],
               ['x', '16', 'x', 'x', '13', '17', '14', '6', '2', '17', '19', '6', '13', '6'],
               ['x', '1', 'x', 'x', '3', '10', '2', '18', '7', '8', 'x', '8', 'x', 'x'],
               ['12', '2', '1', '6', '11', '7', '10', 'x', 'x', 'x', '4', '2', '8', 'x'],
               ['x', 'x', 'x', '13', '16', '2', 'x', '6', '9', '2', '11', '7', '14', '6'],
               ['x', 'x', 'x', 'x', 'x', 'x', '11', 'x', '10', 'x', 'x', 'x', '14', '6']]
   num_rows = 13
   num_cols = 14
   start = (1, 13)
   end = (7, 4)
   districts = [(0, 1), (2, 6), (7, 13)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and it's in a different district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city map, it's not an 'x', and it's in a different district
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(start_row <= new_row <= end_row for start_row, end_row in districts) and
               any(start_col <= new_col <= end_col for start_col, end_col in districts)):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
