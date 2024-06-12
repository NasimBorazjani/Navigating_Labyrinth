
import heapq


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 0)
   goal_state = (6, 6)
   # Define the matrix map of the city
   city_map = [['x', 'x', '6', 'x', '7', 'x', '9', '4', '11'],
               ['x', '3', 'x', '6', '5', '3', '15', 'x', '3'],
               ['x', 'x', 'x', '4', 'x', '9', '1', '8', 'x'],
               ['15', '18', '1', '6', '5', '10', '6', '14', '8'],
               ['18', '10', '7', '18', '2', 'x', 'x', 'x', '7'],
               ['11', '9', '16', 'x', '11', 'x', '11', 'x', '17'],
               ['7', 'x', '18', 'x', '8', '10', '20', '6', 'x'],
               ['15', '4', '17', 'x', '16', '2', '12', '16', 'x'],
               ['9', '10', '18', '17', '9', '6', '7', 'x', '15']]
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(9):
       for j in range(9):
           if city_map[i][j] != 'x':
               if i < 4:
                   districts[0].add((i, j))
               elif i < 7:
                   districts[1].add((i, j))
               else:
                   districts[2].add((i, j))


   visited_costs = {}
   visited_costs[(initial_state, frozenset())] = 0


   queue = [(0, 0, [], initial_state, frozenset())]


   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)


       if state == goal_state and len(visited_districts) == 3:
           return actions


       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < 9 and 0 <= new_col < 9 and city_map[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_visited_districts = visited_districts.copy()
               for i, district in enumerate(districts):
                   if new_state in district:
                       new_visited_districts.add(i)
               new_cost = g + int(city_map[new_row][new_col])
               if (new_state, frozenset(new_visited_districts)) not in visited_costs or new_cost < visited_costs[(new_state, frozenset(new_visited_districts))]:
                   visited_costs[(new_state, frozenset(new_visited_districts))] = new_cost
                   h = heuristic(new_state, goal_state)
                   heapq.heappush(queue, (g + h, new_cost, actions + [new_state], new_state, frozenset(new_visited_districts)))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the shortest path from the current state to the goal state is the Manhattan distance
   # The heuristic is consistent because the cost of moving from one state to a neighboring state is always 1, which is exactly the decrease in the Manhattan distance, if the state is moved toward the goal state, otherwise the estimated cost of the successor state is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
