
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['10', 'x', '19', '11', 'x', 'x', '6', '12', 'x', 'x', 'x'],
               ['2', '9', '10', 'x', 'x', '10', '17', 'x', 'x', '11', '5'],
               ['x', '15', '8', '9', 'x', '7', '17', '20', 'x', 'x', '13'],
               ['1', '9', '15', '14', '9', '9', '13', '7', '12', 'x', '10'],
               ['9', 'x', '17', 'x', 'x', '7', 'x', 'x', '1', '14'],
               ['16', '18', '11', 'x', '14', '18', '9', '13', 'x', 'x', 'x'],
               ['9', '3', '5', '8', '17', '15', '19', 'x', '3', 'x', '14'],
               ['2', '13', 'x', 'x', '17', '13', '14', '18', '9', 'x', '6'],
               ['3', 'x', '18', '6', 'x', '14', 'x', 'x', '8', '19'],
               ['2', '4', 'x', 'x', 'x', 'x', '3', '4', 'x', '19', 'x'],
               ['x', 'x', 'x', 'x', '11', 'x', 'x', 'x', 'x', '5', '5']]
   num_rows = 10
   num_cols = 11
   start = (3, 7)
   end = (7, 0)
   districts = [(0, 2), (3, 6), (7, 10)]


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


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # Check if the new state visits at least one workshop in each district
               if all(start_row <= new_row <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))


   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in a valid direction
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It's consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of sqrt(2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
