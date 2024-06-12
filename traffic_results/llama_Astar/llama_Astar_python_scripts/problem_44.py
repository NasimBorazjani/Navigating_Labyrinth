
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 16, 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'],
               ['x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'],
               ['x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14],
               ['x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5],
               [2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19],
               [19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10],
               ['x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15],
               [2, 'x', 11, 9, 'x', 12, 11, 'x', 15, 10, 6],
               [19, 'x', 16, 5, 'x', 'x', 'x', 11, 'x', 11, 8],
               [12, 2, 'x', 'x', 'x', 'x', 15, 'x', 12, 13, 'x']]
   # Define the start and end positions
   start = (8, 10)
   end = (3, 4)
   # Define the districts
   districts = [(0, 2), (3, 7), (8, 10)]
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
           # Check if the new state is valid, ie within the city map, not an x, and in the same district as the current state
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


def heuristic(state, end):
   # An admissible and consistent heuristic for this problem is the Euclidean distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always increases the heuristic cost of the successor node by a value that is equal to or less than the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
