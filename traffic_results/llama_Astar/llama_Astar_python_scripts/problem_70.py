
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['13', 'x', '10', '17', 'x', '4'],
               ['17', 'x', '8', '11', '7', 'x', 'x', '19', 'x', '11', 'x', '13', '18'],
               ['15', '6', '2', '12', '16', '7', 'x', '14', 'x', '2', 'x', '14', '4'],
               ['x', '18', '4', 'x', 'x', 'x', '13', '14', '2', '4', '20', '10', '7'],
               ['7', '2', '19', '16', 'x', 'x', 'x', '18', 'x', 'x', 'x', '2', '2'],
               ['10', '17', '14', '7', '17', '3', '3', '19', 'x', '19', 'x', 'x', '9'],
               ['9', 'x', 'x', 'x', '5', '18', '13', '6', 'x', 'x', 'x', 'x', '19', '10'],
               ['x', 'x', 'x', 'x', 'x', '2', '7', '4', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', '6', '3', 'x', '1', 'x', '14', 'x', '18', 'x', '1', 'x'],
               ['14', 'x', '4', '18', '14', '12', 'x', 'x', 'x', 'x', '2', 'x', '13'],
               ['12', 'x', '3', '1', '12', '9', 'x', '6', 'x', 'x', 'x', '16', 'x', '18'],
               ['13', 'x', '11', '5', '3', '4', 'x', 'x', 'x', 'x', 'x', 'x', '18'],
               ['15', '9', '9', '1', 'x', '6', 'x', 'x', '14', 'x', 'x', '1', '14']]
   # Define the start and end positions
   start = (5, 1)
   end = (2, 11)
   # Define the districts
   districts = [(0, 1), (2, 5), (6, 12)]
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in the same district
       for move in moves:
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie within the city map, not an 'x' workshop, and in the same district as the current state
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1])):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as each move in the heuristic cost of the successor node is a max of 1
   # It's consistent because moving to a workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district as the current one), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
