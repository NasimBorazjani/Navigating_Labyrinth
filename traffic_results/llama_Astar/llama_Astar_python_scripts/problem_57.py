
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['17', '9', '11', '5', '19', '4', '18', 'x', '5', '8', 'x', 'x'],
               ['6', '13', 'x', '9', '2', '20', '11', '20', '7', 'x', 'x', '3'],
               ['4', '17', 'x', '18', '2', '10', 'x', '16', 'x', '18', 'x', 'x'],
               ['12', '10', '9', '14', 'x', 'x', '12', '6', '1', '2', 'x', 'x'],
               ['5', 'x', 'x', '3', 'x', '4', '9', '14', '8', 'x', '10', '12'],
               ['1', 'x', '6', '3', '18', '18', '17', '17', '10', 'x', 'x', '10'],
               ['13', 'x', 'x', 'x', 'x', 'x', '14', 'x', '1', '19', 'x', '7'],
               ['11', 'x', 'x', '5', '9', 'x', '18', '19', '13', '13', 'x', '10'],
               ['x', 'x', '11', 'x', 'x', 'x', 'x', '14', '17', 'x', '13', 'x'],
               ['19', 'x', 'x', 'x', '19', '12', '7', '3', '14', 'x', '9', 'x'],
               ['x', '12', '7', '15', '1', 'x', '16', '11', '9', '17', 'x', 'x']]
   # Define the start and end positions
   start = (7, 0)
   end = (3, 8)
   # Define the districts
   districts = [(0, 3), (4, 6), (7, 11)]
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


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


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in the same district
       for move in moves:
           # Calculate the new position
           new_pos = (current[0] + move[0], current[1] + move[1])
           # Check if the new position is valid, ie within the city map, not an 'x' and in the same district as the current position
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x' and
               any(districts[i][0] <= new_pos[0] <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= current[0] <= districts[i][1])):
               # The new state is valid
               new_state = new_pos
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(current, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the end position
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in the same district
   # It is admissible because it never overestimates the cost to reach the end state
   # It's consistent because moving to a workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district but not in the same row or column), which is equal to the cost of reaching the successor node
   return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
