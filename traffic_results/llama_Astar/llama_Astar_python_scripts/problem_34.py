
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['12', '11', '14', '10', '2', '11', '13', '16', '3', 'x', '12'],
               ['10', '9', 'x', '8', 'x', 'x', '1', '16', '11', 'x', '15'],
               ['1', '18', '1', 'x', 'x', 'x', 'x', 'x', '12', '9', 'x'],
               ['1', '14', '15', '10', '7', '15', '17', '10', '15', '15', '6'],
               ['18', '11', 'x', 'x', 'x', '15', 'x', 'x', '1', '1', 'x'],
               ['14', 'x', 'x', 'x', '18', '14', '16', '7', 'x', '1', 'x'],
               ['11', '15', 'x', 'x', '15', '3', '11', '13', 'x', 'x', 'x'],
               ['5', 'x', 'x', 'x', 'x', 'x', '15', 'x', '6', 'x', 'x'],
               ['12', '11', '7', '2', '11', 'x', '10', '2', '17', 'x', 'x'],
               ['7', 'x', 'x', 'x', '4', 'x', '4', 'x', 'x', '5', 'x'],
               ['x', '19', '10', '7', 'x', '2', '3', '9', '2', '6', 'x']]
   # Define the start and end positions
   start = (7, 0)
   end = (2, 9)
   # Define the districts
   districts = [(0, 2), (3, 6), (7, 10)]
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions from the current position, provided there's no 'x' in that direction
       for move in moves:
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie within the city map boundaries and there's no 'x' in the new state
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and city_map[new_state[0]][new_state[1]] != 'x'):
               # Check if the new state is in a different district from the start state
               if any(start[0] <= new_state[0] <= end[0] <= end[0] or start[1] <= new_state[1] <= end[1] <= end[1] for start, end in districts):
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Euclidean distance from the current state to the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
