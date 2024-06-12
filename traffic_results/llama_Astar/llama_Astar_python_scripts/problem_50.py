
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['12', '17', '10', 'x', 'x', 'x', 'x', '9', '15', '5', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', '12', '20', '9', '19', '8', '12', '11'],
               ['9', 'x', 'x', '2', 'x', '2', '1', '9', '8', '14', '16', 'x'],
               ['19', 'x', '1', '20', '7', '9', '18', 'x', '18', '7', 'x', 'x'],
               ['5', '2', '11', '9', 'x', '5', '4', '16', 'x', '1', 'x', '10'],
               ['10', '8', '8', '4', '11', '11', 'x', 'x', '5', 'x', 'x', 'x'],
               ['15', '15', 'x', 'x', '13', '5', '19', 'x', 'x', '15', 'x', 'x'],
               ['15', '16', '9', '18', 'x', 'x', '16', 'x', 'x', 'x', '5', '12'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', '14', '14', 'x', 'x', '15', '6', '6', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', '8', '14', 'x', '5', 'x', 'x', 'x', '15'],
               ['x', '6', '15', 'x', 'x', 'x', 'x', 'x', '8', 'x', 'x', 'x']]
   # Define the start and end positions
   start = (3, 9)
   end = (7, 1)
   # Define the districts
   districts = [(0, 3), (4, 6), (7, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path taken to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in the same district
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_state = (state[0] + dx, state[1] + dy)
           # Check if the new state would be valid, ie the new state is within the city map, there's no 'x' at the new state, and the new state is in the same district as the current state
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] < districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] < districts[i][1])):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the successor node
   # It is consistent because moving to a neighboring workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the new workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
