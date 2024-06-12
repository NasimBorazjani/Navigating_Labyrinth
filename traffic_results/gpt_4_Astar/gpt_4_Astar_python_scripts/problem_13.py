
import heapq
import numpy as np


def a_star():
   # Define the initial state and the goal state of the problem
   initial_state = (3, 7)
   goal_state = (5, 0)
   # Define the map of the city
   city_map = [['x', 'x', 'x', 'x', '9', 'x', '20', '3', '9'],
               ['17', '11', '17', 'x', '9', '2', '7', 'x', '15'],
               ['x', '4', '2', '19', '12', '6', 'x', '4', '17'],
               ['15', 'x', 'x', '15', '11', '19', 'x', '9', '5'],
               ['3', '9', '19', '15', '2', 'x', 'x', '18', 'x'],
               ['19', '5', '9', '11', '9', 'x', 'x', '3', 'x'],
               ['x', 'x', '2', '8', '8', 'x', 'x', 'x', '19'],
               ['x', 'x', '14', 'x', 'x', 'x', '18', 'x', '18'],
               ['x', '14', '18', '7', '8', 'x', '10', '15', 'x']]
   # Define the districts
   districts = [set(), set(), set()]
   for i in range(9):
       for j in range(9):
           if city_map[i][j] != 'x':
               if i < 4:
                   districts[0].add((i, j))
               elif i == 4:
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
   # The heuristic relaxes the constraint that Ben has to visit at least 1 workshop in each district and presumes Ben can move directly to the goal state
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Ben moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself is 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
