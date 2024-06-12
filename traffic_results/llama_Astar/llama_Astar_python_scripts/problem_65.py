
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['11', 'x', 'x', 'x', '15', '5', '18', '4', '1', '17', '14', 'x', '9'],
               ['x', '10', '10', '7', '12', '12', '6', 'x', 'x', '8', '4', '19', '11'],
               ['17', 'x', 'x', '12', '8', 'x', 'x', 'x', '14', '19', 'x', '18', '16'],
               ['17', 'x', '16', 'x', 'x', '17', '4', 'x', '15', 'x', 'x', 'x', '17'],
               ['17', 'x', 'x', '6', 'x', '12', '6', '10', '3', '11', 'x', '19', '11'],
               ['10', 'x', '9', '15', '17', '4', 'x', 'x', 'x', 'x', '14', '17', '18'],
               ['4', 'x', 'x', 'x', 'x', '13', '18', '13', 'x', '17', '12', 'x', '19'],
               ['x', '2', '11', '7', '6', '14', '9', 'x', '12', '17', '9', '13', '14'],
               ['x', '18', '16', 'x', 'x', 'x', '11', '6', '12', 'x', 'x', '10', 'x'],
               ['5', '3', 'x', 'x', 'x', '5', 'x', '14', 'x', 'x', 'x', 'x', 'x'],
               ['18', 'x', 'x', 'x', 'x', '14', 'x', '13', '1', '3', 'x', 'x', '18'],
               ['1', '16', '10', 'x', 'x', '14', '13', 'x', '10', 'x', '1', 'x', '18'],
               ['8', 'x', 'x', '10', '2', '10', 'x', 'x', 'x', 'x', 'x', '13', '5']]
   # Define the start and end positions
   start = (8, 11)
   end = (2, 3)
   # Define the districts
   districts = [(0, 2), (3, 7), (8, 12)]
   # Define the possible moves
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for move in moves:
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie within the city map boundaries, the new state is not an 'x' and the new state is in a different district from the start state
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if i != state[0] // 3)):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, end)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district from the start state), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
