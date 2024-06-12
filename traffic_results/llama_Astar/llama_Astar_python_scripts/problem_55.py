
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['9', '4', '16', '7', 'x', 'x', 'x', '14', 'x', 'x', 'x'],
               ['x', '15', '10', '5', '12', '16', 'x', 'x', 'x', '3', '12', '18'],
               ['12', 'x', 'x', 'x', '9', '16', '3', '9', 'x', 'x', 'x', '7'],
               ['10', '6', '3', '10', 'x', 'x', '1', '17', 'x', 'x', 'x', '12'],
               ['11', '8', '15', 'x', '8', '16', 'x', 'x', '5', '15', '12', '7'],
               ['x', 'x', 'x', 'x', '6', 'x', '11', '19', '17', '17', '10', '20'],
               ['x', '3', '17', '17', 'x', 'x', '18', '4', 'x', 'x', '9', '4'],
               ['x', '1', '5', '17', '8', '15', '4', '17', '5', '6', '9', '11'],
               ['x', 'x', '4', '5', '17', '18', '3', 'x', '9', '1', '11', '2'],
               ['x', 'x', '5', '3', '4', '14', '14', '1', '17', '3', '12', '12'],
               ['x', '15', '9', '7', '3', 'x', 'x', 'x', 'x', 'x', '17', 'x'],
               ['x', 'x', '13', '16', '6', 'x', '6', 'x', 'x', 'x', 'x', 'x']]
   # Define the start and end positions
   start = (3, 9)
   end = (7, 1)
   # Define the districts
   districts = [(0, 3), (4, 8), (9, 11)]


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


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_state = (state[0] + dx, state[1] + dy)
           # Check if the new state would be valid, ie within the city map boundaries, not moving to a closed workshop, and visiting at least one workshop in each district
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and
               city_map[new_state[0]][new_state[1]] != 'x' and
               all(start[0] <= new_state[0] <= end[0] or
                   any(start[0] <= new_state[0] <= end[0] for start, end in districts) for _ in range(3))):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic for this problem is the Euclidean distance from the current state to the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
